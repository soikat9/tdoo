# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Website Sale Gift Card",
    'summary': "Use gift card in eCommerce",
    'description': """Integrate gift card mechanism in your ecommerce.""",
    'category': 'Website/Website',
    'version': '1.0',
    'depends': ['website_sale', 'sale_gift_card'],
    'data': [
        'views/template.xml',
        'views/gift_card_views.xml',
        'views/gift_card_menus.xml',
        ],
    'demo': [
        'data/product_demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_sale_gift_card/static/**/*',
        ],
    },
    'license': 'LGPL-3',
}
