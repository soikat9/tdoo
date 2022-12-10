# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # technical field used to reconcile the journal items in Tele as they were in Winbooks
    winbooks_matching_number = fields.Char(help="Matching number that was used in Winbooks")
