# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "MRP Barcode",
    'category': 'Inventory/Inventory',
    'version': '1.0',
    'depends': ['stock_barcode', 'mrp'],
    'auto_install': True,
    'application': False,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_qweb': [
            'stock_barcode_mrp/static/src/**/*.xml',
        ],
    }
}
