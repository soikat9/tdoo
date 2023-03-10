# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class AccountPaymentMethod(models.Model):
    _inherit = 'account.payment.method'

    @api.model
    def _get_payment_method_information(self):
        res = super()._get_payment_method_information()
        currency_codes = ['BGN', 'HRK', 'CZK', 'DKK', 'GIP', 'HUF', 'ISK', 'CHF', 'NOK', 'PLN', 'RON', 'SEK', 'GBP', 'EUR']
        currency_ids = self.env['res.currency'].with_context(active_test=False).search([('name', 'in', currency_codes)])
        res['sepa_ct'] = {
            'mode': 'multi',
            'domain': [('type', '=', 'bank')],
            'currency_ids': currency_ids.ids,
        }
        return res
