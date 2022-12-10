# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models

from tele import api, SUPERUSER_ID


def _validate_existing_work_entry(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['hr.work.entry'].search([])._check_if_error()
