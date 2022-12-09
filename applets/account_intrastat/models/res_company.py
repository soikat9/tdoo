# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    intrastat_region_id = fields.Many2one('account.intrastat.code', string='Intrastat region',
        domain="[('type', '=', 'region'), '|', ('country_id', '=', None), ('country_id', '=', country_id)]")
    intrastat_transport_mode_id = fields.Many2one('account.intrastat.code', string='Default Transport Mode',
        domain="[('type', '=', 'transport')]")
