# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_l10n_fr_hr_payroll = fields.Boolean(string='French Payroll')
    module_l10n_be_hr_payroll = fields.Boolean(string='Belgium Payroll')
    module_l10n_in_hr_payroll = fields.Boolean(string='Indian Payroll')
    module_hr_payroll_account = fields.Boolean(string='Payroll with Accounting')
    module_hr_payroll_account_sepa = fields.Boolean(string='Payroll with SEPA payment')
