# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Stock enterprise",
    'version': "1.0",
    'category': 'Inventory/Inventory',
    'summary': "Advanced features for Stock",
    'description': """
Contains the enterprise views for Stock management
    """,
    'depends': ['stock', 'web_dashboard', 'web_cohort', 'web_map', 'web_grid'],
    'data': [
        'security/ir.model.access.csv',
        'security/stock_enterprise_security.xml',
        'views/stock_move_views.xml',
        'views/stock_picking_map_views.xml',
        'report/stock_report_views.xml',
        'report/report_stock_quantity.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': ['stock'],
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'stock_enterprise/static/**/*',
        ],
    }
}
