#-*- coding:utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Work Entries - Contract Enterprise',
    'category': 'Human Resources/Employees',
    'sequence': 39,
    'summary': 'Manage work entries',
    'description': "",
    'installable': True,
    'depends': [
        'hr_work_entry_contract',
    ],
    'data': [
        'views/hr_payroll_menu.xml',
        'views/hr_work_entry_views.xml',
    ],
    'auto_install': True,
    'assets': {
        'web.assets_backend': [
            'hr_work_entry_contract_enterprise/static/**/*',
        ],
    },
    'license': 'TEEL-1',
}
