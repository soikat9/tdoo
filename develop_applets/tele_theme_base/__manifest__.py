# -*- coding: utf-8 -*-
{
    'name': "tele_theme_base",

    'summary': """
        Base for tele tele themes, it support free login for tele
    """,

    'description': """
    """,

    'author': "Tele INC",
    'license': 'TPL-1',
    'category': 'Theme/Backend',
    'version': '1.0.0.1',
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
