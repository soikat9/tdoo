# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Account Invoice Expiry',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'summary': 'This module adds an expiry feature to transaction account intrastat codes.',
    'depends': ['account_intrastat'],
    'data': [
        'data/account.intrastat.code.csv',
        'views/account_intrastat_code_view.xml',
        'views/account_invoice_view.xml',
        'views/product_views.xml',
        'views/report_financial.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
