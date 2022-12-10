# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Point of Sale Discounts',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Simple Discounts in the Point of Sale ',
    'description': """

This module allows the cashier to quickly give percentage-based
discount to a customer.

""",
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_discount_views.xml',
        ],
    'installable': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_discount/static/src/js/**/*',
        ],
        'web.assets_qweb': [
            'pos_discount/static/src/xml/**/*',
        ],
    },
    'license': 'LGPL-3',
}
