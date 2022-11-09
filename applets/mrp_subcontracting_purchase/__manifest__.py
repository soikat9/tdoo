# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Purchase and Subcontracting Management',
    'version': '0.1',
    'category': 'Manufacturing/Purchase',
    'description': """
        This bridge module adds some smart buttons between Purchase and Subcontracting
    """,
    'depends': ['mrp_subcontracting', 'purchase_mrp'],
    'data': [
        'views/purchase_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
