# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Margins by Products',
    'category': 'Sales/Sales',
    'description': """
Adds a reporting menu in products that computes sales, purchases, margins and other interesting indicators based on invoices.
=============================================================================================================================

The wizard to launch the report has several options to help you get the data you need.
""",
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/product_margin_view.xml',
        'views/product_product_views.xml'
    ],
    'license': 'LGPL-3',
}