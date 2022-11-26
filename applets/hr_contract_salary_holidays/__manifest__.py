# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Salary Configurator - Holidays',
    'category': 'Human Resources',
    'summary': 'Automatically creates extra time-off on contract signature',
    'depends': [
        'hr_contract_salary',
        'hr_holidays',
    ],
    'description': """
    """,
    'data': [
        'views/hr_contract_views.xml',
        'views/res_config_settings_views.xml',
        'data/hr_holidays_data.xml',
    ],
    'demo': [
    ],
    'license': 'TEEL-1',
    'auto_install': True,
}
