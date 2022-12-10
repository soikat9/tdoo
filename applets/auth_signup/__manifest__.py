# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Signup',
    'description': """
Allow users to sign up and reset their password
===============================================
    """,
    'version': '1.0',
    'category': 'Hidden/Tools',
    'auto_install': True,
    'depends': [
        'base_setup',
        'mail',
        'web',
    ],
    'data': [
        'data/ir_config_parameter_data.xml',
        'data/ir_cron_data.xml',
        'data/mail_template_data.xml',
        'views/res_config_settings_views.xml',
        'views/res_users_views.xml',
        'views/auth_signup_login_templates.xml',
        ],
    'bootstrap': True,
    'assets': {
        'web.assets_frontend': [
            'auth_signup/static/**/*',
        ],
    },
    'license': 'LGPL-3',
}
