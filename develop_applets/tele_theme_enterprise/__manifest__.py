# -*- coding: utf-8 -*-
{
    'name': "tele_theme_enterprise",

    'summary': """
        
    """,

    'description': """

    """,

    'author': "tele theme",
    'category': 'Theme/backend',
    'version': '1.0.0.3',

    'images': ['static/description/tele_description.gif', 'static/description/tele_screenshot.gif'],

    'price': 99,
    'license': 'TPL-1',
    'depends': ['base', 'web', 'base_setup', 'tele_theme_base', 'tele_theme_setting', 'web_enterprise', 'tele_login'],

    'data': [
        'data/default_mode_datas.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'tele_theme_enterprise/static/css/tele_variables.scss',
            'tele_theme_enterprise/static/css/tele_common.scss',
            'tele_theme_enterprise/static/css/tele_action_manager.scss',
            'tele_theme_enterprise/static/css/tele_sidebar.scss',
            'tele_theme_enterprise/static/css/tele_button.scss',
            'tele_theme_enterprise/static/css/tele_header.scss',
            'tele_theme_enterprise/static/css/tele_discuss.scss',
            'tele_theme_enterprise/static/css/tele_chat.scss',
            'tele_theme_enterprise/static/css/tele_overlay.scss',
            'tele_theme_enterprise/static/css/perfect_scrollbar.css',
            'tele_theme_enterprise/static/css/tele_board.scss',
            'tele_theme_enterprise/static/css/tele_scrollbar.scss',
            'tele_theme_enterprise/static/css/tele_datetime_picker.scss',
            'tele_theme_enterprise/static/css/tele_select2.scss',
            'tele_theme_enterprise/static/css/tele_company.scss',
            'tele_theme_enterprise/static/css/tele_pager.scss',
            'tele_theme_enterprise/static/css/tele_control_panel.scss',
            'tele_theme_enterprise/static/css/tele_footer.scss',
            'tele_theme_enterprise/static/css/tele_kanban.scss',
            'tele_theme_enterprise/static/css/tele_setting.scss',
            'tele_theme_enterprise/static/css/tele_search_panel.scss',
            'tele_theme_enterprise/static/css/tele_misc.scss',
            'tele_theme_enterprise/static/css/tele_accordion.scss',
            'tele_theme_enterprise/static/css/tele_dialog_effect.scss',
            'tele_theme_enterprise/static/css/tele_owl_dialog_effect.scss',
            'tele_theme_enterprise/static/css/tele_search_view.scss',
            'tele_theme_enterprise/static/css/tele_rtl.scss',

            'tele_theme_enterprise/static/lib/jquery.fullscreen.js',
            'tele_theme_enterprise/static/lib/perfect-scrollbar.min.js',

            'tele_theme_enterprise/static/src/components/overlay/tele_overlay.js',
            'tele_theme_enterprise/static/src/components/overlay/tele_overlay_service.js',
            'tele_theme_enterprise/static/src/components/sidebar_menu/tele_sidebar_app_item.js',
            'tele_theme_enterprise/static/src/components/sidebar_menu/tele_sidebar_tab_pane.js',
            'tele_theme_enterprise/static/src/components/sidebar_menu/tele_sidebar_menu.js',
            'tele_theme_enterprise/static/src/components/header/tele_header.js',
            'tele_theme_enterprise/static/src/components/user_profile/user_profile.js',
            'tele_theme_enterprise/static/src/components/app_board/tele_app_board.js',
            'tele_theme_enterprise/static/src/components/app_board/tele_app_board_service.js',
            'tele_theme_enterprise/static/src/components/full_screen/tele_full_screen.js',
            'tele_theme_enterprise/static/src/components/footer/tele_footer.js',
            'tele_theme_enterprise/static/src/components/accordion/tele_accordion.js',

            'tele_theme_enterprise/static/src/tele_search_panel.js',
            'tele_theme_enterprise/static/src/tele_action_container.js',
            'tele_theme_enterprise/static/src/tele_switch_company.js',
            'tele_theme_enterprise/static/src/tele_list_controller.js',
            'tele_theme_enterprise/static/src/tele_owl_dialog.js',
            'tele_theme_enterprise/static/src/tele_list_render.js',
            'tele_theme_enterprise/static/src/tele_abstract_view.js',
            'tele_theme_enterprise/static/src/tele_view_dialog.js',
            'tele_theme_enterprise/static/src/tele_abstract_controller.js',

            'tele_theme_enterprise/static/js/tele_many2one.js',
            'tele_theme_enterprise/static/js/tele_datetime_picker.js',
            'tele_theme_enterprise/static/js/tele_selection.js',
            'tele_theme_enterprise/static/js/tele_legacy_control_panel.js',
            'tele_theme_enterprise/static/js/tele_basic_controller.js',
            'tele_theme_enterprise/static/js/tele_search_options.js',
            'tele_theme_enterprise/static/js/tele_relation_fields.js',
            'tele_theme_enterprise/static/js/tele_form_render.js',
            'tele_theme_enterprise/static/js/tele_action_menu.js',
            'tele_theme_enterprise/static/js/tele_dialog_extend.js',

            'tele_theme_enterprise/static/src/webclient.js'
        ],

        'web.assets_qweb': [

            'tele_theme_enterprise/static/xml/tele_webclient.xml',
            'tele_theme_enterprise/static/xml/tele_many2one.xml',
            'tele_theme_enterprise/static/xml/tele_selection.xml',
            'tele_theme_enterprise/static/xml/tele_control_pannel.xml',
            'tele_theme_enterprise/static/xml/tele_legacy_control_panel.xml',
            'tele_theme_enterprise/static/xml/tele_pager.xml',
            'tele_theme_enterprise/static/xml/tele_search_panel.xml',
            'tele_theme_enterprise/static/xml/tele_custom_filter_item.xml',
            'tele_theme_enterprise/static/xml/tele_custom_group_by_item.xml',
            'tele_theme_enterprise/static/xml/tele_custom_favorite_item.xml',
            'tele_theme_enterprise/static/xml/tele_misc.xml',
            'tele_theme_enterprise/static/xml/tele_status_button.xml',
            'tele_theme_enterprise/static/xml/tele_action_menu.xml',
            'tele_theme_enterprise/static/xml/tele_owl_dialog.xml',

            'tele_theme_enterprise/static/xml/tele_groupby_menu.xml',
            'tele_theme_enterprise/static/xml/tele_filter_menu.xml',
            'tele_theme_enterprise/static/xml/tele_comparision_menu.xml',
            'tele_theme_enterprise/static/xml/tele_favorite_menu.xml',

            'tele_theme_enterprise/static/src/components/sidebar_menu/tele_sidebar_menu.xml',
            'tele_theme_enterprise/static/src/components/header/tele_header.xml',
            'tele_theme_enterprise/static/src/components/app_board/tele_app_board.xml',
            'tele_theme_enterprise/static/src/components/full_screen/tele_full_screen.xml',
            'tele_theme_enterprise/static/src/components/footer/tele_footer.xml',
            'tele_theme_enterprise/static/src/components/accordion/tele_accordion.xml'
        ],

        'web.assets_backend_prod_only': [
            ('replace', 'web_enterprise/static/src/main.js', 'tele_theme_enterprise/static/src/main.js'),
        ]
    }
}
