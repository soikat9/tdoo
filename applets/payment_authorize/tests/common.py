# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.payment.tests.common import PaymentCommon


class AuthorizeCommon(PaymentCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)

        cls.authorize = cls._prepare_acquirer('authorize', update_values={
            'authorize_login': 'dummy',
            'authorize_transaction_key': 'dummy',
            'authorize_signature_key': '00000000',
            'authorize_currency_id': cls.currency_usd.id,
        })

        cls.acquirer = cls.authorize
        cls.currency = cls.currency_usd
