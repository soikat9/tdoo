# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Pad on tasks',
    'category': 'Services/Project',
    'description': """
This module adds a PAD in all project form views.
=================================================
    """,
    'depends': [
        'project',
        'pad'
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/project_views.xml',
        ],
    'auto_install': True,
    'assets': {
        'web.assets_frontend': [
            'pad_project/static/**/*',
        ],
    },
    'license': 'LGPL-3',
}
