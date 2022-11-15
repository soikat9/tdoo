# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    is_donation = fields.Boolean(string="Is Donation", related="payment_transaction_id.is_donation", help="Is the payment a donation")
