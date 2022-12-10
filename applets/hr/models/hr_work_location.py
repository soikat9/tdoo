# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class WorkLocation(models.Model):
    _name = "hr.work.location"
    _description = "Work Location"
    _order = 'name'

    active = fields.Boolean(default=True)
    name = fields.Char(string="Work Location", required=True)
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    address_id = fields.Many2one('res.partner', required=True, string="Work Address", domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    location_number = fields.Char()
