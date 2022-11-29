# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Helpdesk Sale Coupon',
    'category': 'Services/Helpdesk',
    'summary': 'Project, Tasks, Sale Coupon',
    'depends': ['helpdesk_sale', 'sale_coupon'],
    'auto_install': False,
    'description': """
Generate Coupons from Helpdesks tickets
    """,
    'data': [
        'security/ir.model.access.csv',
        'wizard/helpdesk_sale_coupon_generate_views.xml',
        'views/helpdesk_views.xml',
    ],
    'demo': ['data/helpdesk_sale_coupon_demo.xml'],
    'license': 'TEEL-1',
}
