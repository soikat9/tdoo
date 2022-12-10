# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': 'Base import module',
    'description': """
Import a custom data module
===========================

This module allows authorized users to import a custom data module (.xml files and static assests)
for customization purpose.
""",
    'category': 'Hidden/Tools',
    'depends': ['web'],
    'installable': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'views/base_import_module_view.xml'
    ],
    'license': 'LGPL-3',
}
