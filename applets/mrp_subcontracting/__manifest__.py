# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "mrp_subcontracting",
    'version': '0.1',
    'summary': "Subcontract Productions",
    'description': "",
    'website': 'https://www.tele.studio/app/manufacturing',
    'category': 'Manufacturing/Manufacturing',
    'depends': ['mrp'],
    'data': [
        'data/mrp_subcontracting_data.xml',
        'views/mrp_bom_views.xml',
        'views/res_partner_views.xml',
        'views/stock_warehouse_views.xml',
        'views/stock_move_views.xml',
        'views/stock_quant_views.xml',
        'views/stock_picking_views.xml',
        'views/supplier_info_views.xml',
        'views/product_views.xml',
        'views/mrp_production_views.xml',
        'wizard/stock_picking_return_views.xml',
        'report/mrp_report_bom_structure.xml',
    ],
    'demo': [
        'data/mrp_subcontracting_demo.xml',
    ],
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}
