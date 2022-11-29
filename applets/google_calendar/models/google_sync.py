# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import logging
from contextlib import contextmanager
from functools import wraps
from requests import HTTPError
import pytz
from dateutil.parser import parse

from tele import api, fields, models, registry, _
from tele.tools import ormcache_context
from tele.exceptions import UserError
from tele.osv import expression

from tele.applets.google_calendar.utils.google_event import GoogleEvent
from tele.applets.google_calendar.utils.google_calendar import GoogleCalendarService
from tele.applets.google_account.models.google_service import TIMEOUT

_logger = logging.getLogger(__name__)


# API requests are sent to Google Calendar after the current transaction ends.
# This ensures changes are sent to Google only if they really happened in the Tele database.
# It is particularly important for event creation , otherwise the event might be created
# twice in Google if the first creation crashed in Tele.
def after_commit(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        dbname = self.env.cr.dbname
        context = self.env.context
        uid = self.env.uid

        if self.env.context.get('no_calendar_sync'):
            return

        @self.env.cr.postcommit.add
        def called_after():
            db_registry = registry(dbname)
            with db_registry.cursor() as cr:
                env = api.Environment(cr, uid, context)
                try:
                    func(self.with_env(env), *args, **kwargs)
                except Exception as e:
                    _logger.warning("Could not sync record now: %s" % self)
                    _logger.exception(e)

    return wrapped

@contextmanager
def google_calendar_token(user):
    yield user._get_google_calendar_token()


class GoogleSync(models.AbstractModel):
    _name = 'google.calendar.sync'
    _description = "Synchronize a record with Google Calendar"

    google_id = fields.Char('Google Calendar Id', copy=False)
    need_sync = fields.Boolean(default=True, copy=False)
    active = fields.Boolean(default=True)

    def write(self, vals):
        google_service = GoogleCalendarService(self.env['google.service'])
        if 'google_id' in vals:
            self._from_google_ids.clear_cache(self)
        synced_fields = self._get_google_synced_fields()
        if 'need_sync' not in vals and vals.keys() & synced_fields and not self.env.user.google_synchronization_stopped:
            vals['need_sync'] = True

        result = super().write(vals)
        for record in self.filtered('need_sync'):
            if record.google_id:
                record._google_patch(google_service, record.google_id, record._google_values(), timeout=3)

        return result

    @api.model_create_multi
    def create(self, vals_list):
        if any(vals.get('google_id') for vals in vals_list):
            self._from_google_ids.clear_cache(self)
        if self.env.user.google_synchronization_stopped:
            for vals in vals_list:
                vals.update({'need_sync': False})
        records = super().create(vals_list)

        google_service = GoogleCalendarService(self.env['google.service'])
        records_to_sync = records.filtered(lambda r: r.need_sync and r.active)
        for record in records_to_sync:
            record._google_insert(google_service, record._google_values(), timeout=3)
        return records

    def unlink(self):
        """We can't delete an event that is also in Google Calendar. Otherwise we would
        have no clue that the event must must deleted from Google Calendar at the next sync.
        """
        synced = self.filtered('google_id')
        # LUL TODO find a way to get rid of this context key
        if self.env.context.get('archive_on_error') and self._active_name:
            synced.write({self._active_name: False})
            self = self - synced
        elif synced:
            # Since we can not delete such an event (see method comment), we archive it.
            # Notice that archiving an event will delete the associated event on Google.
            # Then, since it has been deleted on Google, the event is also deleted on Tele DB (_sync_google2tele).
            self.action_archive()
            return True
        return super().unlink()

    @api.model
    @ormcache_context('google_ids', keys=('active_test',))
    def _from_google_ids(self, google_ids):
        if not google_ids:
            return self.browse()
        return self.search([('google_id', 'in', google_ids)])

    def _sync_tele2google(self, google_service: GoogleCalendarService):
        if not self:
            return
        if self._active_name:
            records_to_sync = self.filtered(self._active_name)
        else:
            records_to_sync = self
        cancelled_records = self - records_to_sync

        updated_records = records_to_sync.filtered('google_id')
        new_records = records_to_sync - updated_records
        for record in cancelled_records.filtered(lambda e: e.google_id and e.need_sync):
            record._google_delete(google_service, record.google_id)
        for record in new_records:
            record._google_insert(google_service, record._google_values())
        for record in updated_records:
            record._google_patch(google_service, record.google_id, record._google_values())

    def _cancel(self):
        self.google_id = False
        self.unlink()

    @api.model
    def _sync_google2tele(self, google_events: GoogleEvent, default_reminders=()):
        """Synchronize Google recurrences in Tele. Creates new recurrences, updates
        existing ones.

        :param google_recurrences: Google recurrences to synchronize in Tele
        :return: synchronized tele recurrences
        """
        existing = google_events.exists(self.env)
        new = google_events - existing - google_events.cancelled()

        tele_values = [
            dict(self._tele_values(e, default_reminders), need_sync=False)
            for e in new
        ]
        new_tele = self.with_context(dont_notify=True)._create_from_google(new, tele_values)
        cancelled = existing.cancelled()
        cancelled_tele = self.browse(cancelled.tele_ids(self.env))
        cancelled_tele._cancel()
        synced_records = new_tele + cancelled_tele
        for gevent in existing - cancelled:
            # Last updated wins.
            # This could be dangerous if google server time and tele server time are different
            updated = parse(gevent.updated)
            tele_record = self.browse(gevent.tele_id(self.env))
            # Migration from 13.4 does not fill write_date. Therefore, we force the update from Google.
            if not tele_record.write_date or updated >= pytz.utc.localize(tele_record.write_date):
                vals = dict(self._tele_values(gevent, default_reminders), need_sync=False)
                tele_record.with_context(dont_notify=True)._write_from_google(gevent, vals)
                synced_records |= tele_record

        return synced_records

    def _google_error_handling(self, http_error):
        # We only handle the most problematic errors of sync events.
        if http_error.response.status_code in (403, 400):
            response = http_error.response.json()
            if not self.exists():
                reason = "Google gave the following explanation: %s" % response['error'].get('message')
                error_log = "Error while syncing record. It does not exists anymore in the database. %s" % reason
                _logger.error(error_log)
                return 

            if self._name == 'calendar.event':
                start = self.start and self.start.strftime('%Y-%m-%d at %H:%M') or _("undefined time")
                event_ids = self.id
                name = self.name
                error_log = "Error while syncing event: "
                event = self
            else:
                # calendar recurrence is triggering the error
                event = self.base_event_id or self._get_first_event(include_outliers=True)
                start = event.start and event.start.strftime('%Y-%m-%d at %H:%M') or _("undefined time")
                event_ids = _("%(id)s and %(length)s following", id=event.id, length=len(self.calendar_event_ids.ids))
                name = event.name
                # prevent to sync other events
                self.calendar_event_ids.need_sync = False
                error_log = "Error while syncing recurrence [{id} - {name} - {rrule}]: ".format(id=self.id, name=self.name, rrule=self.rrule)

            # We don't have right access on the event or the request paramaters were bad.
            # https://developers.google.com/calendar/v3/errors#403_forbidden_for_non-organizer
            if http_error.response.status_code == 403 and "forbiddenForNonOrganizer" in http_error.response.text:
                reason = _("you don't seem to have permission to modify this event on Google Calendar")
            else:
                reason = _("Google gave the following explanation: %s", response['error'].get('message'))

            error_log += "The event (%(id)s - %(name)s at %(start)s) could not be synced. It will not be synced while " \
                         "it is not updated. Reason: %(reason)s" % {'id': event_ids, 'start': start, 'name': name,
                                                                    'reason': reason}
            _logger.error(error_log)

            body = _(
                "The following event could not be synced with Google Calendar. </br>"
                "It will not be synced as long at it is not updated.</br>"
                "%(reason)s", reason=reason)

            if event:
                event.message_post(
                    body=body,
                    message_type='comment',
                    subtype_xmlid='mail.mt_note',
                )

    @after_commit
    def _google_delete(self, google_service: GoogleCalendarService, google_id, timeout=TIMEOUT):
        with google_calendar_token(self.env.user.sudo()) as token:
            if token:
                google_service.delete(google_id, token=token, timeout=timeout)
                # When the record has been deleted on our side, we need to delete it on google but we don't want
                # to raise an error because the record don't exists anymore.
                self.exists().with_context(dont_notify=True).need_sync = False

    @after_commit
    def _google_patch(self, google_service: GoogleCalendarService, google_id, values, timeout=TIMEOUT):
        with google_calendar_token(self.env.user.sudo()) as token:
            if token:
                try:
                    google_service.patch(google_id, values, token=token, timeout=timeout)
                except HTTPError as e:
                    if e.response.status_code in (400, 403):
                        self._google_error_handling(e)
                self.exists().with_context(dont_notify=True).need_sync = False

    @after_commit
    def _google_insert(self, google_service: GoogleCalendarService, values, timeout=TIMEOUT):
        if not values:
            return
        with google_calendar_token(self.env.user.sudo()) as token:
            if token:
                try:
                    send_updates = self._context.get('send_updates', True)
                    google_service.google_service = google_service.google_service.with_context(send_updates=send_updates)
                    google_id = google_service.insert(values, token=token, timeout=timeout)
                    # Everything went smoothly
                    self.with_context(dont_notify=True).write({
                        'google_id': google_id,
                        'need_sync': False,
                    })
                except HTTPError as e:
                    if e.response.status_code in (400, 403):
                        self._google_error_handling(e)
                        self.with_context(dont_notify=True).need_sync = False

    def _get_records_to_sync(self, full_sync=False):
        """Return records that should be synced from Tele to Google

        :param full_sync: If True, all events attended by the user are returned
        :return: events
        """
        domain = self._get_sync_domain()
        if not full_sync:
            is_active_clause = (self._active_name, '=', True) if self._active_name else expression.TRUE_LEAF
            domain = expression.AND([domain, [
                '|',
                    '&', ('google_id', '=', False), is_active_clause,
                    ('need_sync', '=', True),
            ]])
        # We want to limit to 200 event sync per transaction, it shouldn't be a problem for the day to day
        # but it allows to run the first synchro within an acceptable time without timeout.
        # If there is a lot of event to synchronize to google the first time,
        # they will be synchronized eventually with the cron running few times a day
        return self.with_context(active_test=False).search(domain, limit=200)

    def _write_from_google(self, gevent, vals):
        self.write(vals)

    @api.model
    def _create_from_google(self, gevents, vals_list):
        return self.create(vals_list)

    @api.model
    def _tele_values(self, google_event: GoogleEvent, default_reminders=()):
        """Implements this method to return a dict of Tele values corresponding
        to the Google event given as parameter
        :return: dict of Tele formatted values
        """
        raise NotImplementedError()

    def _google_values(self):
        """Implements this method to return a dict with values formatted
        according to the Google Calendar API
        :return: dict of Google formatted values
        """
        raise NotImplementedError()

    def _get_sync_domain(self):
        """Return a domain used to search records to synchronize.
        e.g. return a domain to synchronize records owned by the current user.
        """
        raise NotImplementedError()

    def _get_google_synced_fields(self):
        """Return a set of field names. Changing one of these fields
        marks the record to be re-synchronized.
        """
        raise NotImplementedError()

    @api.model
    def _restart_google_sync(self):
        """ Turns on the google synchronization for all the events of
        a given user.
        """
        raise NotImplementedError()
