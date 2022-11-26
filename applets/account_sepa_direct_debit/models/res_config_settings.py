# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sdd_creditor_identifier = fields.Char(related='company_id.sdd_creditor_identifier', string='Creditor Identifier', readonly=False,
        help='Creditor identifier of your company within SEPA scheme.')
