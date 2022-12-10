# coding: utf-8
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class PosPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    def _get_payment_terminal_selection(self):
        return super(PosPaymentMethod, self)._get_payment_terminal_selection() + [('six', 'SIX')]

    six_terminal_ip = fields.Char('Six Terminal IP')
