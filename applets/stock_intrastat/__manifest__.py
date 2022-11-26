# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Stock Intrastat',
    'category': 'Inventory/Inventory',
    'description': """
A module that add the stock management in intrastat reports.
============================================================

This module gives the details of the goods traded between the countries of
European Union.""",
    'depends': ['stock_account', 'account_intrastat'],
    'data': [
        'views/stock_warehouse_view.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
