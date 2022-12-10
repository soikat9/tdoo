# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class LunchLocation(models.Model):
    _name = 'lunch.location'
    _description = 'Lunch Locations'

    name = fields.Char('Location Name', required=True)
    address = fields.Text('Address')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
