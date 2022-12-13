# -*- coding: utf-8 -*-
{
    'name': 'Contacts Maps',
    'version': '1.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Tools',
    'description': """
Contacts Maps
=============

Added Google Map view on contacts
""",
    'depends': [
        'contacts',
        'base_geolocalize',
        'web_google_maps',
        'google_marker_icon_picker'
    ],
    'website': '',
    'data': [
        'views/res_partner.xml',
    ],
    'demo': [],
    'installable': True
}
