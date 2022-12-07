# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Google reCAPTCHA integration',
    'category': 'Hidden',
    'version': '1.0',
    'description': """
        This module implements reCaptchaV3 so that you can prevent bot spam on your public modules.
    """,
    'depends': ['base_setup'],
    'data': [
        'views/res_config_settings_view.xml',
    ],
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'google_recaptcha/static/src/scss/recaptcha.scss',
            'google_recaptcha/static/src/js/recaptcha.js',
        ],
    },
    'license': 'LGPL-3',
}
