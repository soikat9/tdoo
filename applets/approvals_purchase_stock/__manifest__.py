# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': 'Approvals - Purchase - Stock',
    'version': '1.0',
    'category': 'Human Resources/Approvals',
    'description': """ Technical module to link Approvals, Purchase and Inventory together. """,
    'depends': ['approvals_purchase', 'purchase_stock'],
    'data': [
        'views/approval_product_line_views.xml',
        'views/approval_request_views.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
