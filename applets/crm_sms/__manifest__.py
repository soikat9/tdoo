# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'SMS in CRM',
    'version': '1.1',
    'category': 'Sales/CRM',
    'summary': 'Add SMS capabilities to CRM',
    'description': "",
    'depends': ['crm', 'sms'],
    'data': [
        'views/crm_lead_views.xml',
        'security/ir.model.access.csv',
        'security/sms_security.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
