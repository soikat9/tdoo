# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Helpdesk - CRM',
    'summary': 'Convert Tickets from/to Leads',
    'version': '1.1',
    'sequence': '19',
    'category': 'Services/Helpdesk',
    'complexity': 'easy',
    'description': """
Convert business inquiries that have ended up in the Helpdesk pipeline by mistake,
or generate a ticket from a business inquiry
        """,
    'data': [
        'security/ir.model.access.csv',
        'wizard/crm_lead_convert2ticket_views.xml',
        'wizard/helpdesk_ticket_to_lead_views.xml',
        'views/crm_lead_views.xml',
        'views/helpdesk_ticket_views.xml',
    ],
    'depends': ['crm', 'helpdesk'],
    'auto_install': True,
    'license': 'TEEL-1',
}
