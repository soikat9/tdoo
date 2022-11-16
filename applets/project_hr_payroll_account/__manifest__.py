# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Project Payroll Accounting',
    'version': '1.0',
    'category': 'Services/payroll/account',
    'summary': 'Project payroll accounting',
    'description': 'Bridge created to add the number of contracts linked to an AA to a project form',
    'depends': ['project', 'hr_payroll_account'],
    'data': [
        'views/project_project_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
