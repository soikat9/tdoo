# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', company_dependent=True,
        help="Analytic account in which cost and revenue entries will take place for financial management of the manufacturing order.")
