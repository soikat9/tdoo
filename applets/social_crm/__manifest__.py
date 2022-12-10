# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'CRM statistics on social',
    'category': 'Hidden',
    'version': '1.0',
    'summary': 'Add crm UTM info on social',
    'description': """UTM and posts on crm""",
    'depends': ['social', 'crm'],
    'data': [
        'views/social_post_views.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
