# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models


class PeopleSeniority(models.Model):
    """ Seniority for People Rules """
    _name = 'crm.iap.lead.seniority'
    _description = 'People Seniority'

    name = fields.Char(string='Name', required=True, translate=True)
    reveal_id = fields.Char(required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Name already exists!'),
    ]

    @api.depends('name')
    def name_get(self):
        return [(seniority.id, seniority.name.replace('_', ' ').title()) for seniority in self]
