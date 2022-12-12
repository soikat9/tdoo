# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Advanced Menu',
    'version': '1.0.1.0.0',
'sequence': 1,
    'summary': """

    """,
    'description': "It's time to bid goodbye to the boring, monotonous menu of Odoo which you have been using for a while and say hello to a new menu, which breathes life into your Odoo backend.",
    'author': 'NEWAY Solutions',
    'license': 'TPL-1',
    'depends': [
        'web'
    ],
    'data': [
        
    ],
    'assets': {
        'web.assets_qweb': [
            'tele_menu/static/src/xml/menu.xml',
        ],
        'web.assets_backend': [
            'tele_menu/static/src/scss/menu.scss',
        ],
    },
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
