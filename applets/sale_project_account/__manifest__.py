# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Project Sales Accounting',
    'version': '1.0',
    'category': 'Services/account',
    'summary': 'Project sales accounting',
    'description': 'Bridge created to add the number of vendor bills linked to an AA to a project form',
    'depends': ['sale_timesheet', 'account'],
    'data': [
        'views/project_project_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
