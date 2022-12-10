# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'POS Restaurant Adyen',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Adds American style tipping to Adyen',
    'description': '',
    'depends': ['pos_adyen', 'pos_restaurant', 'payment_adyen'],
    'data': [
        'views/pos_payment_method_views.xml',
        ],
    'auto-install': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_restaurant_adyen/static/**/*',
        ],
    },
    'license': 'LGPL-3',
}
