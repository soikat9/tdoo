# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Website Helpdesk',
    'category': 'Hidden',
    'sequence': 57,
    'summary': 'Bridge module for helpdesk modules using the website.',
    'description': 'Bridge module for helpdesk modules using the website.',
    'depends': [
        'helpdesk',
        'website',
    ],
    'data': [
        'views/assets.xml',
        'views/helpdesk_views.xml',
        'views/helpdesk_templates.xml',
    ],
    'license': 'TEEL-1',
    'assets': {
        'web.assets_frontend': [
            'website_helpdesk/static/**/*',
        ],
    }
}
