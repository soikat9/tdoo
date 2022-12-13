# -*- coding: utf-8 -*-
{
    'name': 'CRM Maps',
    'version': '1.0.1.0.2',
    'license': 'AGPL-3',
    'category': 'Sales/CRM',
    'sequence': 100,
    'description': """
CRM Maps
========

Added google_map view on your leads/opportunities
""",
    'depends': ['crm', 'web_google_maps'],
    'website': '',
    'data': [
        'views/crm_lead.xml',
        'views/res_partner.xml',
    ],
    'demo': [],
    'installable': True
}
