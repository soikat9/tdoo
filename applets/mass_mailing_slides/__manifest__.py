# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Mass mailing on course members',
    'category': 'Hidden',
    'version': '1.0',
    'description':
        """
Mass mail course members
========================

Bridge module adding UX requirements to ease mass mailing of course members.
        """,
    'depends': ['website_slides', 'mass_mailing'],
    'data': [
        'views/slide_channel_views.xml'
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
