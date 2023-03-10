# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models, api


class AccountIntrastatCode(models.Model):
    _inherit = ['account.intrastat.code']

    expiry_date = fields.Date(
        string='Expiry Date',
        help='Date at which a code must not be used anymore.',
    )
    start_date = fields.Date(
        string='Usage start date',
        help='Date from which a code may be used.',
    )
