# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele.applets.payment.tests.common import PaymentCommon


class PaypalCommon(PaymentCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)

        cls.paypal = cls._prepare_acquirer('paypal', update_values={
            'paypal_email_account': 'dummy@test.mail.com',
            'fees_active': False,
        })

        # Override default values
        cls.acquirer = cls.paypal
        cls.currency = cls.currency_euro
