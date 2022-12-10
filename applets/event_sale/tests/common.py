# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.event.tests.common import TestEventCommon
from tele.applets.sales_team.tests.common import TestSalesCommon


class TestEventSaleCommon(TestEventCommon, TestSalesCommon):

    @classmethod
    def setUpClass(cls):
        super(TestEventSaleCommon, cls).setUpClass()

        cls.event_product = cls.env['product.product'].create({
            'name': 'Test Registration Product',
            'description_sale': 'Mighty Description',
            'list_price': 10,
            'standard_price': 30.0,
            'detailed_type': 'event',
        })
