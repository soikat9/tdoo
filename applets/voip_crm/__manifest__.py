# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "VOIP for crm",

    'summary': "Link between voip and crm",

    'description': """
Adds the lead partner to phonecall list
    """,

    'category': 'Sales/CRM',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'voip'],
    'auto_install': True,
    # always loaded
    'data': [
        'views/crm_lead_views.xml'
    ],
    'application': False,
    'license': 'TEEL-1',
}
