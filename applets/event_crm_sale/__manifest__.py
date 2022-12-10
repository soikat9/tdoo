# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Event CRM Sale',
    'version': '1.0',
    'category': 'Marketing/Events',
    'website': 'https://www.tele.studio/app/events',
    'description': "Add information of sale order linked to the registration for the creation of the lead.",
    'depends': ['event_crm', 'event_sale'],
    'data': [
        'views/event_lead_rule_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
