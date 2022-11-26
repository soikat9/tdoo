# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Documents - HR',
    'version': '1.0',
    'category': 'Productivity/Documents',
    'summary': 'Access documents from the employee profile',
    'description': """
Easily access your documents from your employee profile.
""",
    'website': ' ',
    'depends': ['documents', 'hr'],
    'data': [
        'data/documents_hr_data.xml',
        'views/res_config_settings_views.xml',
        'views/hr_employee_views.xml',
        'views/res_users_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
