# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Product Availability Notifications',
    'category': 'Website/Website',
    'summary': 'Notify the user when a product is back in stock',
    'description': """
Allow the user to select if he wants to receive email notifications when a product of his wishlist gets back in stock.
    """,
    'depends': [
        'website_sale_stock',
        'website_sale_wishlist',
    ],
    'data': [
        'views/templates.xml',
        'data/template_email.xml',
        'data/ir_cron_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_sale_stock_wishlist/static/src/**/*',
        ],
    },
    'auto_install': True,
    'license': 'LGPL-3',
}
