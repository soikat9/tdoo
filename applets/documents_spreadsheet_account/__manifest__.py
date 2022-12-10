# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': "Spreadsheet Accounting Templates",
    'version': '1.0',
    'category': 'Productivity/Documents',
    'summary': 'Spreadsheet Accounting templates',
    'description': 'Spreadsheet Accounting templates',
    'depends': ['documents_spreadsheet', 'account'],
    'data': [
        'data/documents_data.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_tests': [
            'documents_spreadsheet_account/static/**/*',
        ],
    }
}
