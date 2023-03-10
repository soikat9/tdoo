# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Import OFX Bank Statement',
    'category': 'Accounting/Accounting',
    'version': '1.0',
    'depends': ['account_bank_statement_import'],
    'description': """
Module to import OFX bank statements.
======================================

This module allows you to import the machine readable OFX Files in Tele: they are parsed and stored in human readable format in
Accounting \ Bank and Cash \ Bank Statements.

Bank Statements may be generated containing a subset of the OFX information (only those transaction lines that are required for the
creation of the Financial Accounting records).
    """,
    'data': [
        'wizard/account_bank_statement_import_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
