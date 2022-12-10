# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': "Documents Spreadsheet",
    'version': '1.0',
    'category': 'Productivity/Documents',
    'summary': 'Documents Spreadsheet',
    'description': 'Documents Spreadsheet',
    'depends': ['documents'],
    'data': [
        'data/documents_data.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/documents_views.xml',
        'views/documents_templates.xml',
        'views/res_config_settings_views.xml',
        'wizard/save_spreadsheet_template.xml',
    ],
    'demo': [
        'demo/documents_demo_data.xml'
    ],

    'application': False,
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'documents_spreadsheet/static/src/**/*.js',
            'documents_spreadsheet/static/src/scss/**/*',
            ('remove', 'documents_spreadsheet/static/src/legacy/**/*.js')
        ],
        'web.assets_backend_prod_only': [
            'documents_spreadsheet/static/src/legacy/**/*.js',
        ],
        'web.qunit_suite_tests': [
            'documents_spreadsheet/static/tests/**/*',
        ],
        'web.assets_tests': [
            'documents_spreadsheet/static/tests/tours/**/*',
        ],
        'web.assets_qweb': [
            'documents_spreadsheet/static/src/**/*.xml',
        ],
    }
}
