# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Automated Action based on Employee Contracts',
    'version': '1.0',
    'category': 'Human Resources',
    'description': """
Bridge to add contract calendar on automated actions
====================================================
    """,
    'depends': ['base_automation', 'hr_contract'],
    'data': [
        'views/base_automation_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
