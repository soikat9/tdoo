# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Field Service Stock',
    'category': 'Hidden',
    'summary': 'Validate stock moves for product added on sales orders through Field Service Management App',
    'description': """
Validate stock moves for Field Service
======================================
""",
    'depends': ['industry_fsm_sale', 'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_product_views.xml',
        'wizard/fsm_stock_tracking_views.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
