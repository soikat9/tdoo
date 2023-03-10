# -*- encoding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Quality checks with IoT',
    'category': 'Manufacturing/Internet of Things (IoT)',
    'summary': 'Control the quality of your products with IoT devices',
    'description': """
Use devices connected to an IoT Box to control the quality of your products.
""",
    'depends': ['quality_control', 'iot'],
    'data': [
        'wizard/quality_check_wizard_views.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
