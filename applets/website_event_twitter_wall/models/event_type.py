# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models

class EventType(models.Model):
    _inherit = "event.type"

    social_menu = fields.Boolean(
        'Twitter Wall Menu Item', compute='_compute_social_menu',
        readonly=False, store=True)

    @api.depends('website_menu')
    def _compute_social_menu(self):
        for event_type in self:
            event_type.social_menu = event_type.website_menu
