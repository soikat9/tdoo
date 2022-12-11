# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


class Company(models.Model):
    _inherit = "res.company"

    # here, key has to be full xmlID(including the module name) of all the
    # new report actions that you have defined for check layout
    account_check_printing_layout = fields.Selection(selection_add=[
        ('l10n_us_check_printing.action_print_check_top', 'Print Check (Top) - US'),
        ('l10n_us_check_printing.action_print_check_middle', 'Print Check (Middle) - US'),
        ('l10n_us_check_printing.action_print_check_bottom', 'Print Check (Bottom) - US'),
    ], ondelete={
        'l10n_us_check_printing.action_print_check_top': 'set default',
        'l10n_us_check_printing.action_print_check_middle': 'set default',
        'l10n_us_check_printing.action_print_check_bottom': 'set default',
    })