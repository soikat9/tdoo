# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Point of Sale enterprise',
    'category': 'Sales/Point of Sale',
    'summary': 'Advanced features for PoS',
    'description': """
Advanced features for the PoS like better views 
for IoT Box config.   
""",
    'data': [
        'views/pos_config_view.xml',
    ],
    'depends': ['web_enterprise', 'point_of_sale'],
    'auto_install': True,
    'license': 'TEEL-1',
}
