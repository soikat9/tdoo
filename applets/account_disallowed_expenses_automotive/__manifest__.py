# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': 'Disallowed Expenses on Automotives',
    'category': 'Accounting/Accounting',
    'summary': 'Manage disallowed expenses with automotives',
    'description': "",
    'version': '1.0',
    'depends': ['account_automotive', 'account_disallowed_expenses'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_disallowed_expenses_category_views.xml',
        'views/account_move_views.xml',
        'views/automotive_vehicle_views.xml',
        'views/report_financial.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
    'license': 'TEEL-1',
}
