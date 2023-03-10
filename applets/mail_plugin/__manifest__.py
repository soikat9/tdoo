# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Mail Plugin',
    'version': '1.0',
    'category': 'Sales/CRM',
    'sequence': 5,
    'summary': 'Allows integration with mail plugins.',
    'description': "Integrate Tele with your mailbox, get information about contacts directly inside your mailbox, log content of emails as internal notes",
    'depends': [
        'web',
        'contacts',
        'iap'
    ],
    'web.assets_backend': [
        'mail_plugin/static/src/to_translate/**/*',
    ],
    'data': [
        'views/mail_plugin_login.xml',
        'views/res_partner_iap_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
