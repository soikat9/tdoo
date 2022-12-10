# -*- coding: utf-8 -*-
{
    'name': "tele_theme_base",

    'summary': """
        
    """,

    'description': """

    """,
    'license': 'TPL-1',
    'images': ['static/description/screen_shot.png', 'static/description/banner.png'],
    'category': 'Theme/Backend',
    'version': '1.0.0.7',

    'installable': True,
    'application': True,
   'auto_install': False,

    'depends': ['base', 'web'],
    
    'data': [
        "views/tele_web.xml"
    ],

    'assets': {
        'web.assets_backend': [
            'tele_theme_base/static/css/tele_variables.scss',

            'tele_theme_base/static/css/mixins/_flex.scss',
            'tele_theme_base/static/css/mixins/_box_shadow.scss',
            'tele_theme_base/static/css/mixins/_clearfix.scss',
            'tele_theme_base/static/css/mixins/_float.scss',
            'tele_theme_base/static/css/mixins/_hover.scss',
            'tele_theme_base/static/css/mixins/_gradients.scss',
            'tele_theme_base/static/css/mixins/_buttons.scss',
            
            'tele_theme_base/static/css/tele_functions.scss',

            'tele_theme_base/static/css/tele_form_controls.scss',
            'tele_theme_base/static/css/tele_buttons.scss',

            'tele_theme_base/static/css/tele_form_view.scss',
            'tele_theme_base/static/css/tele_list_view.scss',
            'tele_theme_base/static/css/tele_scroll.scss',
            'tele_theme_base/static/css/tele_misc.scss',

            'tele_theme_base/static/js/tele_form_controller.js',
            'tele_theme_base/static/js/tele_customizer.js',
        ],
        
        'web.assets_qweb': [ 
            'tele_theme_base/static/xml/misc.xml'
        ]
    }
}
