# -*- coding: utf-8 -*-
{
    'name': 'Contacts Google Places Autocomplete',
    'version': '1.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Base',
    'sequence': 1000,
    'description': """
Contact Google Places Autocomplete
==================================

Use Google Address Form autocomplete to help you find address
""",
    'depends': [
        'base_geolocalize',
        'web_google_maps',
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'demo': [],
    'installable': True
}
