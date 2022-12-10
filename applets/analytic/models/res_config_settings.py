# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_analytic_accounting = fields.Boolean(string='Analytic Accounting', implied_group='analytic.group_analytic_accounting')
