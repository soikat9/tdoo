# -*- coding: utf-8 -*-
{
    'name': 'Contact Google Address Form Extended',
    'version': '1.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Base',
    'sequence': 1000,
    'description': """
Contact Google Address Form
===========================

Use Google Address Form autocomplete to help you find address
""",
    'depends': [
        'base_address_extended',
        'contacts_google_address_form',
        'web_google_maps',
    ],
    'data': ['views/res_partner.xml'],
    'demo': [],
    'installable': True,
}
