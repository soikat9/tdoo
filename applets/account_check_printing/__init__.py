# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import api, SUPERUSER_ID
from . import models
from . import wizard


def create_check_sequence_on_bank_journals(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['account.journal'].search([('type', '=', 'bank')])._create_check_sequence()
