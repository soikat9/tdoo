# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class EventBoothCategory(models.Model):
    _name = 'event.booth.category'
    _description = 'Event Booth Category'
    _inherit = ['image.mixin']
    _order = 'sequence ASC'

    active = fields.Boolean(default=True)
    name = fields.Char(string='Name', required=True, translate=True)
    sequence = fields.Integer(string='Sequence', default=10)
    description = fields.Html(string='Description', translate=True)
    booth_ids = fields.One2many('event.booth', 'booth_category_id', string='Booths')
