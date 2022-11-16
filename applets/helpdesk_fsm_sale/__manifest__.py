# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': 'Helpdesk FSM - Sale',
    'description': """
        Bridge between Helpdesk and Industry FSM Sale
    """,
    'summary': 'Project, Helpdesk, FSM, Timesheet and Sale Orders',
    'category': 'Hidden',
    'depends': ['helpdesk_fsm', 'helpdesk_sale_timesheet', 'industry_fsm_sale'],
    'data': [
        'views/project_project_views.xml',
    ],
    'demo': [],
    'auto_install': True,
    'license': 'TEEL-1',
}
