# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Contacts Enterprise',
    'summary': 'Enterprise features on contacts',
    'description': 'Adds notably the map view of contact',
    'category': 'Sales/CRM',
    'version': '1.0',
    'depends': [
        'contacts',
        'web_map'
    ],
    'data': [
        "views/contact_views.xml"
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
