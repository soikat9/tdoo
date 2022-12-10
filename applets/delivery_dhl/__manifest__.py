# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': "DHL Express Shipping",
    'description': "Send your shippings through DHL and track them online",
    'category': 'Inventory/Delivery',
    'sequence': 285,
    'version': '1.0',
    'application': True,
    'depends': ['delivery', 'mail'],
    'data': [
        'data/delivery_dhl_data.xml',
        'views/delivery_dhl_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'TEEL-1',
}
