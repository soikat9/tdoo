# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Sell Helpdesk Timesheet',
    'category': 'Hidden',
    'summary': 'Project, Helpdesk, Timesheet and Sale Orders',
    'depends': ['helpdesk_timesheet', 'sale_timesheet', 'helpdesk_sale'],
    'description': """
        Bill timesheets logged on helpdesk tickets.
    """,
    'auto_install': True,
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_views.xml',
        'views/helpdesk_portal_templates.xml',
        'views/project_project_views.xml',
        'views/product_views.xml',
        'views/sale_views.xml',
    ],
    'demo': ['data/helpdesk_sale_timesheet_demo.xml'],
    'license': 'TEEL-1',
    'post_init_hook': '_helpdesk_sale_timesheet_post_init'
}
