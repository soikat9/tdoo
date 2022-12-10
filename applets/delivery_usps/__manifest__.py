# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': "United States Postal Service (USPS) Shipping",
    'description': "Send your shippings through USPS and track them online",
    'category': 'Inventory/Delivery',
    'sequence': 305,
    'version': '1.0',
    'application': True,
    'depends': ['delivery', 'mail'],
    'data': [
        'data/delivery_usps_data.xml',
        'views/delivery_usps_view.xml',
        'views/delivery_usps_template.xml',
        'views/res_config_settings_views.xml',
    ],
    'license': 'TEEL-1',
}
