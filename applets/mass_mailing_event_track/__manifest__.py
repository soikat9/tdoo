# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Mass mailing on track speakers',
    'category': 'Hidden',
    'version': '1.0',
    'description':
        """
Mass mail event track speakers
==============================

Bridge module adding UX requirements to ease mass mailing of event track speakers.
        """,
    'depends': ['website_event_track', 'mass_mailing'],
    'data': [
        'views/event_views.xml'
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
