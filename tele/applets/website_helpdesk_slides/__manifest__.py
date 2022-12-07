# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Website Slides Helpdesk',
    'category': 'Services/Helpdesk',
    'sequence': 58,
    'summary': 'Ticketing, Support, Slides',
    'depends': [
        'website_helpdesk',
        'website_slides',
    ],
    'description': """
Website Slides integration for the helpdesk module
==================================================

    Add slide presentations to your team so customers seeking help can see them those before submitting new tickets.

    """,
    'data': [
        'views/helpdesk_views.xml',
        'views/helpdesk_templates.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
    'post_init_hook': '_website_helpdesk_slides_post_init',
}
