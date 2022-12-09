# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Website Partner',
    'category': 'Hidden',
    'summary': 'Partner module for website',
    'version': '0.1',
    'description': """
This is a base module. It holds website-related stuff for Contact model (res.partner).
    """,
    'depends': ['website'],
    'data': [
        'views/res_partner_views.xml',
        'views/website_partner_templates.xml',
        'data/website_partner_data.xml',
    ],
    'demo': ['data/website_partner_demo.xml'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
