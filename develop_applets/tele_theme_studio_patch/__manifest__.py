# -*- coding: utf-8 -*-
{
    'name': "tele_theme_studio_patch",

    'summary': """
        this this the tele theme studio patch, it is used to add a new menu item to the studio menu""",

    'description': """
        studio patch for tele theme
    """,

    'website': "https://www.tele.studio/?fw=2",

    'category': 'Theme/Backend',
    'version': '1.0.0.1',

    'depends': ['base', 'tele_studio', 'tele_theme_enterprise'],

    'data': [],

    'assets': {
        'web.assets_backend': [
            'tele_theme_studio_patch/static/css/style.scss',

            ('remove', 'tele_studio/static/src/home_menu/home_menu.js'),
            ('remove', 'tele_studio/static/src/systray_item/systray_item.js'),

            'tele_theme_studio_patch/static/src/app_board_patch.js',
            'tele_theme_studio_patch/static/src/studio_service.js',
            'tele_theme_studio_patch/static/src/systray_item/systray_item.js',
        ],

        'web.assets_qweb': [
            ('remove', 'tele_studio/static/src/home_menu/home_menu.xml'),
            'tele_theme_studio_patch/static/xml/app_board.xml',
            'tele_theme_studio_patch/static/src/systray_item/systray_item.xml',
        ]
    }
}
