# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': "IoT for Delivery",
    'summary': "Use IoT devices in delivery operations",
    'description': """
Allows using IoT devices, such as scales and printers, for delivery operations.
""",
    'category': 'Manufacturing/Internet of Things (IoT)',
    'version': '1.0',
    'depends': ['iot', 'delivery'],
    'data': [
        'wizard/choose_delivery_package_views.xml',
        'views/iot_views.xml',
        'views/stock_picking_views.xml',
        ],
    'license': 'TEEL-1',
    'auto_install': True,
    'assets': {
        'web.assets_backend': [
            'delivery_iot/static/src/js/**/*',
        ],
        'web.assets_qweb': [
            'delivery_iot/static/src/xml/**/*',
        ],
    }
}
