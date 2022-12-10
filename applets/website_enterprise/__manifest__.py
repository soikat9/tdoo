# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': 'Website Enterprise',
    'category': 'Hidden',
    'summary': 'Get the enterprise look and feel',
    'description': """
This module overrides community website features and introduces enterprise look and feel.
    """,
    'depends': ['website'],
    'data': [
        'data/website_data.xml',
        'views/website_enterprise_templates.xml'
    ],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_frontend': [
            'website_enterprise/static/src/**/*',
        ],
    }
}
