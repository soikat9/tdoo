# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Sale statistics on social',
    'category': 'Hidden',
    'version': '1.0',
    'summary': 'Add sale UTM info on social',
    'description': """UTM and post on sale orders""",
    'depends': ['social', 'sale'],
    'data': [
        'views/social_post_views.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
