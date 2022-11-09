# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': "IAP / Mail",
    'summary': """Bridge between IAP and mail""",
    'description': """Bridge between IAP and mail""",
    'category': 'Hidden/Tools',
    'version': '1.0',
    'depends': [
        'iap',
        'mail',
    ],
    'application': False,
    'installable': True,
    'auto_install': True,
    'data': [
        'data/mail_templates.xml',
    ],
    'license': 'LGPL-3',
}
