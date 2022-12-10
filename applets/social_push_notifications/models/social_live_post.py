# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import ast
import pytz

from tele import models, fields, _
from tele.osv import expression


class SocialLivePostPushNotifications(models.Model):
    _inherit = 'social.live.post'

    reached_visitor_ids = fields.Many2many('website.visitor', string="Reached Visitors")

    def _post(self):
        """ The _post method of push notifications, unlike other social.media, doesn't post messages directly
        Instead, we keep them 'ready' and they are gathered by a cron job (see 'social.post#_cron_publish_scheduled'). """

        push_notifications_live_posts = self.filtered(lambda post: post.account_id.media_type == 'push_notifications')
        super(SocialLivePostPushNotifications, (self - push_notifications_live_posts))._post()

        push_notifications_live_posts.write({
            'state': 'ready'
        })

    def _post_push_notifications(self):
        for live_post in self:
            post = live_post.post_id
            account = live_post.account_id
            title = post.push_notification_title or _('New Message')
            icon_url = '/social_push_notifications/social_post/%s/push_notification_image' % post.id if post.push_notification_image else '/mail/static/src/img/telebot_transparent.png'

            # TODO awa: force push_token domain here in case user manually removed it in form view?
            visitor_domain = ast.literal_eval(live_post.post_id.visitor_domain)
            target_link = ''
            if post.push_notification_target_url:
                link_tracker_values = live_post._get_utm_values()
                link_tracker_values['url'] = post.push_notification_target_url
                link_tracker = self.env['link.tracker'].search_or_create(link_tracker_values)
                target_link = link_tracker.short_url

            if not post.use_visitor_timezone or not post.scheduled_date:
                target_visitors = self.env['website.visitor'].search(visitor_domain)
            else:
                # We need to filter the target_visitors based on their timezone
                post_date = post.scheduled_date
                post_user_datetime = pytz.utc.localize(post_date).astimezone(pytz.timezone(post.create_uid.tz)).replace(tzinfo=None)
                now_utc = pytz.utc.localize(fields.Datetime.now())

                def get_filtered_timezone_visitors(visitor):
                    visitor_tz = pytz.timezone(visitor.timezone or 'UTC')
                    visitor_local_datetime = now_utc.astimezone(visitor_tz).replace(tzinfo=None)
                    return visitor_local_datetime > post_user_datetime

                pending_visitors = self.env['website.visitor'].search(expression.AND([visitor_domain, [('id', 'not in', live_post.reached_visitor_ids.ids)]]))
                target_visitors = pending_visitors.filtered(get_filtered_timezone_visitors)

            account._firebase_send_message({
                'title': title,
                'body': live_post.message,
                'icon': icon_url,
                'target_url': target_link
            }, target_visitors)

            # TODO awa:
            # In theory, we should clean registrations from database for which we receive a 'registration-token-not-registered' error.
            # However, while running tests, I've seen that this error appears a lot more than it should.
            # When looking into it, I've seen this topic: https://github.com/firebase/firebase-admin-node/issues/533
            # It mentions how this error is kind of like a 'default' and could mean many things (firebase having issues contacting a service, ...)
            # As long as we can't be sure that the token is actually expired, we can't risk to delete it.
            # 2 possible solutions:
            # - wait for them to break the error down into more specific codes (see github thread)
            # - implement a mechanism where we remove the registration after having received X errors consecutively
            # In the mean time, please DON'T UNCOMMENT this
            # self._clean_unregistered_tokens(result)

            if post.use_visitor_timezone:
                values = {
                    'reached_visitor_ids': [(4, target_visitor.id) for target_visitor in target_visitors]
                }
                # If all visitors have been processed
                if len(pending_visitors) == len(target_visitors):
                    values['state'] = 'posted'

                live_post.write(values)
            else:
                live_post.write({'state': 'posted'})

    # TODO AWA : check what is result object and use token directly instead of id
    # as token are now stored on website_visitor
    def _clean_unregistered_tokens(self, result):
        """ This will clean the tokens for which we receive a 'registration-token-not-registered' error
        from firebase.
        This method assumes the 'responses' from the batches are ordered the same way as matching registrations.
        (In all test cases so far, they were) """

        matched_registrations = result[0]
        batch_results = result[1]

        all_responses = []
        for batch_result in batch_results:
            all_responses.extend(batch_result.responses)

        i = 0
        registration_token_to_remove = []
        for response in all_responses:
            i += 1
            if not response.success and response.exception.code == 'registration-token-not-registered':
                registration_token_to_remove.append(matched_registrations[i]['token'])

        if registration_token_to_remove:
            self.env['website.visitor'].search([('push_token', 'in', registration_token_to_remove)]).sudo().write({
                'push_token': False
            })
