# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


def uninstall_hook(cr, registry):
    cr.execute(
        "DELETE FROM ir_model_data WHERE module = 'l10n_generic_coa'"
    )
