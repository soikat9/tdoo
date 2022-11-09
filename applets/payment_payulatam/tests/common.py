# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.payment.tests.common import PaymentCommon


class PayULatamCommon(PaymentCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)

        cls.payulatam = cls._prepare_acquirer('payulatam', update_values={
            'payulatam_account_id': 'dummy',
            'payulatam_merchant_id': 'dummy',
            'payulatam_api_key': 'dummy',
        })

        # Override default values
        cls.acquirer = cls.payulatam
        cls.currency = cls.currency_euro
