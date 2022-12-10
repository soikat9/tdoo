# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class ContractHistory(models.Model):
    _inherit = 'hr.contract.history'

    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', readonly=True)
