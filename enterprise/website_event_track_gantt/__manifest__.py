# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Enterprise Event Track',
    'category': 'Marketing',
    'summary': 'Advanced Event Track Management',
    'version': '1.0',
    'description': """This module helps analyzing and organizing event tracks.
For that purpose it adds a gantt view on event tracks.""",
    'depends': ['website_event_track', 'web_gantt'],
    'auto_install': True,
    'data': [
        'views/event_event_views.xml',
        'views/event_track_views.xml',
    ],
    'license': 'TEEL-1',
}
