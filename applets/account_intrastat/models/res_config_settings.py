# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    company_country_id = fields.Many2one('res.country', string="Company country", readonly=True,
        related='company_id.account_fiscal_country_id')
