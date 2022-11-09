# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Push notification to track listeners',
    'category': 'Marketing/Events',
    'sequence': 1021,
    'version': '1.1',
    'summary': 'Send reminder push notifications to event attendees based on favorites tracks.',
    'website': 'https://www.tele.studio/app/events',
    'description': "",
    'depends': [
        'website_event_social',
        'website_event_track',
    ],
    'data': [
        'views/event_track_views.xml'
    ],
    'demo': [
    ],
    'application': False,
    'installable': True,
    'auto_install': True,
    'post_init_hook': 'post_init',
    'license': 'TEEL-1',
}
