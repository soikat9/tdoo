# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': 'POS Adyen',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Integrate your POS with an Adyen payment terminal',
    'description': '',
    'data': [
        'views/pos_config_views.xml',
        'views/pos_payment_method_views.xml',
    ],
    'depends': ['point_of_sale'],
    'installable': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_adyen/static/**/*',
        ],
    },
    'license': 'LGPL-3',
}
