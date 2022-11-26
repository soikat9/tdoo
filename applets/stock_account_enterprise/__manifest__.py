# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Stock account enterprise",
    'version': "1.0",
    'category': 'Inventory/Inventory',
    'summary': "Advanced features for stock_account",
    'description': """
Contains the enterprise views for Stock account
    """,
    'depends': ['stock_account', 'stock_enterprise', 'web_dashboard'],
    'data': [
        'report/stock_report_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': ['stock_account'],
    'license': 'TEEL-1',
}
