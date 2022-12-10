# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Online Ticket Submission',
    'category': 'Website/Website',
    'sequence': 58,
    'summary': 'Qualify helpdesk queries with a website form',
    'depends': [
        'website_helpdesk',
    ],
    'description': """
Generate tickets in Helpdesk app from a form published on your website. This form can be customized thanks to the *Website Builder*.
    """,
    'data': [
        'data/website_helpdesk.xml',
        'views/helpdesk_templates.xml'
    ],
    'post_init_hook': 'post_install_hook_ensure_team_forms',
    'license': 'TEEL-1',
    'assets': {
        'website.assets_editor': [
            'website_helpdesk_form/static/src/**/*',
        ],
    }
}
