# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class EventRegistration(models.Model):
    _name = 'event.registration'
    _inherit = ['event.registration']

    visitor_id = fields.Many2one('website.visitor', string='Visitor', ondelete='set null')

    def _get_website_registration_allowed_fields(self):
        return {'name', 'phone', 'email', 'mobile', 'event_id', 'partner_id', 'event_ticket_id'}
