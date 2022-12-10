# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "VOIP OnSIP",

    'description': """
Module with the required configuration to connect to OnSIP.
    """,

    'category': 'Hidden',
    'version': '1.0',

    'depends': ['voip'],

    'data': [
        'views/res_config_settings_views.xml',
        'views/res_users_views.xml',
        ],
    'application': False,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'voip_onsip/static/src/**/*',
        ],
    }
}
