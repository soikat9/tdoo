# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Google Spreadsheet',
    'version': '1.0',
    'category': 'Hidden/Tools',
    'description': """
The module adds the possibility to display data from Tele in Google Spreadsheets in real time.
=================================================================================================
""",
    'depends': ['google_drive'],
    'data': [
        'data/google_spreadsheet_data.xml',
        'views/google_spreadsheet_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'google_spreadsheet/static/src/**/*.js',
        ],
        'web.assets_qweb': [
            'google_spreadsheet/static/src/**/*.xml',
        ],
        'web.qunit_suite_tests': [
            'google_spreadsheet/static/tests/**/*',
        ],
    },
    'license': 'LGPL-3',
}
