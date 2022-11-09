# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': "Free Delivery with Coupon on eCommerce",
    'summary': """Allows to offer free shippings in coupon reward on eCommerce""",
    'description': """Allows to offer free shippings in coupon reward on eCommerce""",
    'category': 'Website/Website',
    'version': '1.0',
    'depends': ['website_sale_delivery', 'sale_coupon_delivery'],
    'auto_install': True,
    'assets': {
        'web.assets_frontend': [
            'website_sale_coupon_delivery/static/**/*',
        ],
    },
    'license': 'LGPL-3',
}
