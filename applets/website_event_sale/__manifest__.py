# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Online Event Ticketing",
    'category': 'Website/Website',
    'summary': "Sell event tickets online",
    'description': """
Sell event tickets through eCommerce app.
    """,
    'depends': ['website_event', 'event_sale', 'website_sale'],
    'data': [
        'data/event_data.xml',
        'views/event_event_views.xml',
        'views/website_event_templates.xml',
        'views/website_sale_templates.xml',
        'security/ir.model.access.csv',
        'security/website_event_sale_security.xml',
    ],
    'auto_install': True,
    'assets': {
        'web.assets_tests': [
            'website_event_sale/static/tests/**/*',
        ],
    },
    'license': 'LGPL-3',
}
