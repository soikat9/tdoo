# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class Event(models.Model):
    _inherit = "event.event"

    def action_mass_mailing_track_speakers(self):
        mass_mailing_action = dict(
            name='Mass Mail Attendees',
            type='ir.actions.act_window',
            res_model='mailing.mailing',
            view_mode='form',
            target='current',
            context=dict(
                default_mailing_model_id=self.env.ref('website_event_track.model_event_track').id,
                default_mailing_domain=repr([('event_id', 'in', self.ids), ('stage_id.is_cancel', '!=', True)]),
            ),
        )
        return mass_mailing_action
