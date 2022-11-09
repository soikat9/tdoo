# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "MRP Project",
    'version': '1.0',
    'summary': "Monitor MRP using project",
    'description': "",
    'category': 'Services/Project',
    'depends': ['mrp_account', 'project'],
    'data': [
        'views/project_views.xml',
    ],
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
