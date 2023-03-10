# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Account Winbooks Import",
    'summary': """Import Data From Winbooks""",
    'description': """
        Import Data From Winbooks
    """,
    'category': 'Accounting/Accounting',
    'depends': ['account_accountant', 'base_vat'],
    'external_dependencies': {'python': ['dbfread']},
    'data': [
        'security/ir.model.access.csv',
        'wizard/import_wizard_views.xml',
    ],
    'license': 'TEEL-1',
}
