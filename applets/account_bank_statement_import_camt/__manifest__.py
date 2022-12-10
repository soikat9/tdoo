# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Import CAMT Bank Statement',
    'category': 'Accounting/Accounting',
    'depends': ['account_bank_statement_import'],
    'description': """
Module to import CAMT bank statements.
======================================

Improve the import of bank statement feature to support the SEPA recommended Cash Management format (CAMT.053).
    """,
    'data': [
        'data/account_bank_statement_import_data.xml'
    ],
    'license': 'TEEL-1',
    'auto_install': True,
}
