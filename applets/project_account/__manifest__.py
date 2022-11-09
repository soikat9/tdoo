# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Project Accounting',
    'version': '1.0',
    'category': 'Services/account',
    'summary': 'Project accounting',
    'description': 'Bridge created to remove the profitability setting if the account module is installed',
    'depends': ['project', 'account'],
    'data': [
        'views/project_project_templates.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
