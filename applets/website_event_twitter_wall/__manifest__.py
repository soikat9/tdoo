# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Configure a Twitter Wall on your Event',
    'category': 'Marketing/Events',
    'sequence': 1030,
    'version': '1.1',
    'summary': 'Bridge module to configure a twitter wall on your event',
    'website': 'https://www.tele.studio/app/events',
    'description': "",
    'depends': [
        'website_twitter_wall',
        'website_event',
    ],
    'data': [
        'views/event_event_views.xml',
        'views/event_twitter_wall_templates.xml',
        'views/event_type_views.xml',
    ],
    'demo': [
        'data/event_twitter_wall_demo.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': True,
    'assets': {
        'web.assets_frontend': [
            'website_event_twitter_wall/static/**/*',
        ],
    },
    'license': 'TEEL-1',
}
