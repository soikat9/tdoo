# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Project Accounting Assets',
    'version': '1.0',
    'category': 'Services/assets',
    'summary': 'Project accounting assets',
    'description': 'Bridge created to add the number of assets linked to an AA to a project form',
    'depends': ['project', 'account_asset'],
    'data': [
        'views/project_project_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
