# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': "Fedex Shipping",
    'description': "Send your shippings through Fedex and track them online",
    'category': 'Inventory/Delivery',
    'sequence': 295,
    'version': '1.0',
    'application': True,
    'depends': ['delivery', 'mail'],
    'data': [
        'data/delivery_fedex.xml',
        'views/delivery_fedex.xml',
        'views/res_config_settings_views.xml',
    ],
    'license': 'TEEL-1',
}
