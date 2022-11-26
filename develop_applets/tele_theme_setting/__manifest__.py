# -*- coding: utf-8 -*-
{
    'name': "tele_theme_setting",

    'summary': """
        Theme Setting For Tele
    """,

    'description': """
        Theme setting for tele, common theme setting for tele.
    """,

    'author': "Tele INC",
    'category': 'Theme/Backend',
    'version': '1.0.0.1',
    'installable': True,
    'auto_install': False,

    'images': ['static/description/screen_shot.png',
               'static/description/banner.png',
               'static/description/banner.png'],

    'license': 'TPL-1',
    'depends': ['base', 'web', 'tele_theme_base'],

    'data': [
        'security/ir.model.access.csv',
        
        'views/tele_res_setting.xml',
        'views/tele_theme_mode.xml',
        'views/tele_theme_style.xml',
        'views/tele_theme_style_group.xml',
        'views/tele_theme_style_item.xml',
        'views/tele_theme_style_item_sub_group.xml',
        'views/tele_theme_var.xml',
        'views/tele_user_view.xml',
        'views/tele_company_view.xml',
        'views/tele_import_theme_style.xml',
        'views/tele_web.xml',
        'views/tele_background_image.xml',
        'views/tele_bk_image_wizard.xml',
    ],

    'assets': {
        'web.assets_backend': [
            ('remove', 'tele_theme_base/static/js/tele_customizer.js'),
            
            'tele_theme_setting/static/lib/bootstrap_color_picker/css/bootstrap-colorpicker.min.css',
            'tele_theme_setting/static/lib/bootstrap_color_picker/js/bootstrap-colorpicker.min.js',

            'tele_theme_setting/static/css/tele_customizer.scss',
            'tele_theme_setting/static/js/tele_customizer.js',

            'tele_theme_setting/static/css/tele_setting.scss',
            'tele_theme_setting/static/js/tele_setting.js',
            'tele_theme_setting/static/src/tele_menu_helper.js',

            'tele_theme_setting/static/js/tele_theme_editor.js',
            'tele_theme_setting/static/js/tele_theme_edit_action.js',
            'tele_theme_setting/static/src/theme_editor/tele_theme_editor.js',

            'tele_theme_setting/static/src/tele_webclient.js'
        ],

        'web.assets_qweb': [ 
            'tele_theme_setting/static/xml/customizer.xml'
        ]
    }
}
