# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    costs_hour_account_id = fields.Many2one(
        'account.analytic.account', string='Analytic Account',
        help="Fill this only if you want automatic analytic accounting entries on production orders.")
