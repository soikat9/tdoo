# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Memos pad',
    'version': '0.1',
    'category': 'Productivity/Notes',
    'description': """
This module update memos inside Tele for using an external pad
=================================================================

Use for update your text memo in real time with the following user that you invite.

""",
    'summary': 'Sticky memos, Collaborative',
    'depends': [
        'mail',
        'pad',
        'note',
    ],
    'data': [
        'views/note_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
