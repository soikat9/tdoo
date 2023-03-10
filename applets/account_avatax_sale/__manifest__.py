# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': 'Avatax for SO',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'depends': ['account_avatax', 'sale'],
    'data': [
        'views/sale_order_views.xml',
        'reports/sale_order.xml',
    ],
    'assets': {
        'web.assets_tests': [
            'account_avatax_sale/static/tests/tours/account_avatax_sale_optional_products.js',
        ],
    },
    'auto_install': True,
    'license': 'TEEL-1',
}
