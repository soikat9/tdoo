# -*- coding: utf-8 -*-

{
    "name":   "Web Notification",
    "license": "TPL-1",
    "category": "Website",
    "summary": "Web Push Notification",   
    "description": """This module is useful to create a custom web notification. You can create and send instant web push notifications to users. You can send notifications in 3 ways, popup notification, animation & simple text notification.""",       
    "version": "1.0.3",
    "depends": [
        "base", "web","bus",
    ],
    "application": True,
    "data": [
        "security/base_security.xml",
        "security/ir.model.access.csv",
        "views/annoucement_view.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'sh_web_notification/static/src/js/action_container.js',
            'sh_web_notification/static/src/js/bus_notification.js',
        ]
    },
    "images": ["", ],
    "auto_install": True,
    "installable": True,

}
