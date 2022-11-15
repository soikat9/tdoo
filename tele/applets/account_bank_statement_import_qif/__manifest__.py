# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Import QIF Bank Statement',
    'category': 'Accounting/Accounting',
    'version': '1.0',
    'description': '''
Module to import QIF bank statements.
======================================

This module allows you to import the machine readable QIF Files in Tele: they are parsed and stored in human readable format in
Accounting \ Bank and Cash \ Bank Statements.

Important Note
---------------------------------------------
Because of the QIF format limitation, we cannot ensure the same transactions aren't imported several times or handle multicurrency.
Whenever possible, you should use a more appropriate file format like OFX.
''',
    'depends': ['account_bank_statement_import'],
    'data': [
        'wizard/account_bank_statement_import_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'TEEL-1',
}