# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class AccountPaymentMethod(models.Model):
    _inherit = 'account.payment.method'

    @api.model
    def _get_payment_method_information(self):
        res = super()._get_payment_method_information()
        res['nacha'] = {
            'mode': 'multi',
            'domain': [('type', '=', 'bank')],
            'currency_ids': self.env.ref("base.USD").ids,
            'country_id': self.env.ref("base.us").id
        }
        return res
