# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.account_taxcloud.tests.common import TestAccountTaxcloudCommon
from tele.tests.common import HttpCase
from tele.tests import tagged

@tagged("external")
class TestWebsiteSaleGiftCard(TestAccountTaxcloudCommon, HttpCase):

    def setUp(self):
        super().setUp()

        self.gift_card = self.env['gift.card'].create({
            'initial_amount': 10000,
            'code': '123456',
        })

        self.product_delivery_normal = self.env['product.product'].create({
            'name': 'Normal Delivery Charges',
            'invoice_policy': 'order',
            'type': 'service',
            'list_price': 10.0,
        })

        self.normal_delivery = self.env['delivery.carrier'].create({
            'name': 'Normal Delivery Charges',
            'fixed_price': 5,
            'delivery_type': 'fixed',
            'website_published': True,
            'product_id': self.product_delivery_normal.id,
        })

    def test_01_gift_card_with_taxcloud(self):
        #get admin user
        self.admin_user = self.env.ref('base.user_admin')
        self.admin_user.city = 'Zanesville'
        self.admin_user.state_id = self.env.ref("base.state_us_30").id
        self.admin_user.country_id = self.env.ref('base.us')
        self.admin_user.zip = '43071'
        self.admin_user.street = '226 Adair Ave'
        self.admin_user.property_account_position_id = self.fiscal_position

        self.start_tour("/", 'shop_sale_giftcard', login='admin')
