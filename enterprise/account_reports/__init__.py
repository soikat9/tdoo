# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, SUPERUSER_ID

from . import models
from . import controllers
from . import wizard

def set_periodicity_journal_on_companies(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    for company in env['res.company'].search([]):
        company.account_tax_periodicity_journal_id = company._get_default_misc_journal()