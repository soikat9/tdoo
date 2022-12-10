# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Purchase Stock Enterprise",
    'version': "1.0",
    'category': "Inventory/Purchase",
    'summary': "Customized Dashboard for Purchase Stock",
    'description': "",
    'depends': ['purchase_enterprise', 'purchase_stock'],
    'data': [
        'report/purchase_report_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'TEEL-1',
}
