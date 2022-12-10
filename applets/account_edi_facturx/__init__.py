# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models
from tele import api, SUPERUSER_ID


def _post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    modules = env['ir.module.module'].search([('name', '=', 'account_edi_ubl_cii'), ('state', '=', 'uninstalled')])
    modules.sudo().button_install()
