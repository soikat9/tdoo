# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Helpdesk Repair',
    'category': 'Services/Helpdesk',
    'summary': 'Project, Tasks, Repair',
    'depends': ['helpdesk_stock', 'repair'],
    'auto_install': False,
    'description': """
Repair Products from helpdesk tickets
    """,
    'data': [
        'views/helpdesk_views.xml',
        'views/repair_views.xml',
    ],
    'demo': ['data/helpdesk_repair_demo.xml'],
    'license': 'TEEL-1',
}
