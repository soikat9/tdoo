# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Assets/Automotive bridge',
    'category': 'Accounting/Accounting',
    'summary': 'Manage assets with automotives',
    'description': "",
    'version': '1.0',
    'depends': ['account_automotive', 'account_asset'],
    'data': [
        'views/account_asset_views.xml',
        'views/account_move_views.xml',
    ],
    'license': 'TEEL-1',
    'auto_install': True,
}
