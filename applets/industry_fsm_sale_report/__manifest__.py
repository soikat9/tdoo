# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Field Service Reports - Sale',
    'category': 'Hidden',
    'summary': 'Create Reports for Field service workers',
    'description': """""",
    'depends': ['industry_fsm_sale', 'industry_fsm_report'],
    'data': [
        'report/worksheet_custom_report_templates.xml',
        'views/product_template_views.xml',
        'views/project_views.xml',
        'data/industry_fsm_sale_report_data.xml',
    ],
    'demo': [
        'data/industry_fsm_sale_report_demo.xml',
    ],
    'auto_install': True,
    'post_init_hook': 'post_init',
    'license': 'TEEL-1',
}
