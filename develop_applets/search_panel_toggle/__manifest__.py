# -*- coding: utf-8 -*-

{
    'name': 'Search Panel Hide & Show',
    'summary': """Enable search panel hide & show by a toggle button.""",
    'description': """Search panel hide & show""",

    'version': '1.0.1.1.0',
    'category': 'Extra Tools',
    'license': 'TPL-1',

    # any module necessary for this one to work correctly
    'depends': ['web', 'product'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        #'views/product_search_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'assets': {
        'web.assets_qweb': ['search_panel_toggle/static/src/**/*.xml'],
        'web.assets_backend': [
            'search_panel_toggle/static/src/css/search_panel_toggle.scss',
            'search_panel_toggle/static/src/js/search_panel_toggle.js',

        ],
    }
}
