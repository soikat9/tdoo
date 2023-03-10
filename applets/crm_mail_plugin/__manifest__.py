# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'CRM Mail Plugin',
    'version': '1.0',
    'category': 'Sales/CRM',
    'sequence': 5,
    'summary': 'Turn emails received in your mailbox into leads and log their content as internal notes.',
    'description': "Turn emails received in your mailbox into leads and log their content as internal notes.",
    'website': 'https://www.tele.studio/app/crm',
    'depends': [
        'crm',
        'mail_plugin',
    ],
    'data': [
        'views/crm_mail_plugin_lead.xml',
        'views/crm_lead_views.xml'
    ],
    'web.assets_backend': [
        'crm_mail_plugin/static/src/to_translate/**/*',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
