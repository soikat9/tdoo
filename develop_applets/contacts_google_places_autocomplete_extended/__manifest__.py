# -*- coding: utf-8 -*-
{
    'name': 'Contacts Google Places Autocomplete Extended',
    'version': '1.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Base',
    'sequence': 1000,
    'description': """
Contact Google Places Autocomplete Extended
===========================================

Use Google Places autocomplete to help you find a place
""",
    'depends': [
        'base_address_extended',
        'contacts_google_places_autocomplete',
    ],
    'data': [
        'views/res_partner.xml'
    ],
    'demo': [],
    'installable': True
}
