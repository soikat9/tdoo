# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Mass mailing on sale orders',
    'category': 'Hidden',
    'version': '1.0',
    'summary': 'Add sale order UTM info on mass mailing',
    'description': """UTM and mass mailing on sale orders""",
    'depends': ['sale', 'mass_mailing'],
    'data': [
        'views/mailing_mailing_views.xml',
    ],
    'demo': [
        'data/mass_mailing_demo.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
