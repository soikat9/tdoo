# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Dropship and Subcontracting Management',
    'version': '0.1',
    'category': 'Inventory/Purchase',
    'description': """
        This bridge module allows to manage subcontracting with the dropshipping module.
    """,
    'depends': ['mrp_subcontracting', 'stock_dropshipping'],
    'data': [
        'data/mrp_subcontracting_dropshipping_data.xml',
        'views/stock_warehouse_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
