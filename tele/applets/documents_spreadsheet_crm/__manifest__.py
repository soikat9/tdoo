# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': "Spreadsheet CRM Templates",
    'version': '1.0',
    'category': 'Productivity/Documents',
    'summary': 'Spreadsheet CRM templates',
    'description': 'Spreadsheet CRM templates',
    'depends': ['documents_spreadsheet', 'crm'],
    'data': [
        'data/documents_data.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_tests': [
            'documents_spreadsheet_crm/static/**/*',
        ],
    }
}
