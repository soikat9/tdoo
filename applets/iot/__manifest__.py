# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Internet of Things',
    'category': 'Internet of Things (IoT)',
    'sequence': 250,
    'summary': 'Basic models and helpers to support Internet of Things.',
    'description': """
This module provides management of your IoT Boxes inside Tele.
""",
    'depends': ['mail','web'],
    'data': [
        'wizard/add_iot_box_views.xml',
        'security/ir.model.access.csv',
        'security/iot_security.xml',
        'views/iot_views.xml',
    ],
    'demo': [
        'data/iot_demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'iot/static/src/**/*',
        ],
    }
}
