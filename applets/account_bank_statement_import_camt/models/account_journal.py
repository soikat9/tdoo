# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    def _get_bank_statements_available_import_formats(self):
        rslt = super(AccountJournal, self)._get_bank_statements_available_import_formats()
        rslt.append('CAMT')
        return rslt