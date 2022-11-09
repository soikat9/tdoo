# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class CrmIapLeadIndustry(models.Model):
    """ Industry Tags of Acquisition Rules """
    _name = 'crm.iap.lead.industry'
    _description = 'CRM IAP Lead Industry'
    _order = 'sequence,id'

    name = fields.Char(string='Industry', required=True, translate=True)
    reveal_ids = fields.Char(required=True,
        help="The list of reveal_ids for this industry, separated with ','")
    color = fields.Integer(string='Color Index')
    sequence = fields.Integer('Sequence')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Industry name already exists!'),
    ]
