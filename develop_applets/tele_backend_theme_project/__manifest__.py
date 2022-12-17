# -*- coding: utf-8 -*-
# Part of Tele. See LICENSE file for full copyright and licensing details.

{
    'name': 'Backend Theme Project',
    'category': "Themes/Backend",
    'version': '1.0',
    'license': 'TPL-1',
    'summary': 'Flexible, Powerful and Fully.',
    'description': """ Tele with project
    """,
    'depends': ['project','tele_backend_theme_ent'],
    'images': [
        '',
        '',
    ],
     'assets': {
        'web.assets_qweb': [
            'tele_backend_theme_project/static/src/xml/base.xml',
        ],

    },
    'installable': True,
    'auto_install': False,
    'bootstrap': True,
}
