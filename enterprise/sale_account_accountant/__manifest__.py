# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Sale Accounting",
    'version': "1.0",
    'category': "Sales/Sales",
    'summary': "Bridge between Sale and Accounting",
    'description': """
Notify that a matching sale order exists in the reconciliation widget.
    """,
    'depends': ['sale', 'account_accountant'],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'sale_account_accountant/static/src/js/**/*',
        ],
        'web.assets_qweb': [
            'sale_account_accountant/static/src/xml/**/*',
        ],
    }
}
