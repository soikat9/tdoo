# -*- encoding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Default Theme',
    'description': 'Default website theme',
    'category': 'Theme',
    'sequence': 1000,
    'version': '1.0',
    'depends': ['website'],
    'data': [],
    'images': [
        'static/description/cover.png',
        'static/description/default.png',
    ],
    'snippet_lists': {
        'homepage': ['s_cover', 's_text_image', 's_numbers'],
        'about_us': ['s_text_image', 's_image_text', 's_title', 's_company_team'],
        'our_services': ['s_three_columns', 's_quotes_carousel', 's_references'],
        'pricing': ['s_comparisons'],
        'privacy_policy': ['s_faq_collapse'],
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
