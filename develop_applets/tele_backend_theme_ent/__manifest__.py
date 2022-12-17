# -*- coding: utf-8 -*-
# Part of Tele. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    'name': 'Backend Theme',
    'category': "Themes/Backend",
    'version': '1.0',
    'license': 'TPL-1',
    'summary': 'Enterprise Edition.',
    'description': """ 
    """,
    'depends': ['mail' ,'web_enterprise'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/ir_module_views.xml',
        'views/web_layout_custom.xml',
        'data/theme_data.xml',
        'views/res_users_views.xml',
    ],
    'images': [
        '',
    ],
    'assets': {
        'web.assets_common':[
            '/tele_backend_theme_ent/static/src/js/freamwork/config.js',
        ],
        'web._assets_primary_variables' :    [
            # <!-- link scss variables-->
            "tele_backend_theme_ent/static/src/scss/variables.scss",
            "tele_backend_theme_ent/static/src/scss/other_variable.scss",
            "tele_backend_theme_ent/static/src/scss/night_mode/ni_variables.scss",
        ],
        'web.assets_backend': [
            # <!-- Layout File - Start-->
            "/tele_backend_theme_ent/static/src/lib/minicolors/jquery.minicolors.css",
            "/tele_backend_theme_ent/static/src/scss/animation.scss",
            "/tele_backend_theme_ent/static/src/scss/fonts.scss",
            "/tele_backend_theme_ent/static/src/scss/light_mode/light_mode.scss",

            # Home Menu
            "/tele_backend_theme_ent/static/src/scss/layout/home_menu/home_menu.scss",
            # Left panel
            "/tele_backend_theme_ent/static/src/scss/layout/left_panel/left_menu_horizontal.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/left_panel/left_menu_vertical.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/left_panel/left_menu.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/left_panel/theme_customize_model.scss",
            #control panel
            "/tele_backend_theme_ent/static/src/scss/layout/control_panel/control_panel_search.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/control_panel/control_search_options.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/control_panel/control_action_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/control_panel/control_panel_top.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/control_panel/control_panel_bottom.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/control_panel/control_panel_model.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/control_panel/control_panel.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/control_panel/search_panel.scss",
            # kanban view
            "/tele_backend_theme_ent/static/src/scss/layout/kanban/group_kanban.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/kanban/ungroup_kanban.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/kanban/kanban_model.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/kanban/kanban_view.scss",
            #List View
            "/tele_backend_theme_ent/static/src/scss/layout/list/list_view.scss",
            #calendar view
            "/tele_backend_theme_ent/static/src/scss/layout/calendar/calendar_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/calendar/web_calender.scss",
            # activity view
            "/tele_backend_theme_ent/static/src/scss/layout/activity/activity_view.scss",
            # pivot view
            "/tele_backend_theme_ent/static/src/scss/layout/pivot/pivot_view.scss",
            #discuss
            "/tele_backend_theme_ent/static/src/scss/layout/discuss/composer_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/discuss/message_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/discuss/video_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/discuss/mailbox_mail.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/discuss/chat_view.scss",
            # Form view
            "/tele_backend_theme_ent/static/src/scss/layout/form/form_statusbar.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/form/button_box.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/form/notbook_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/form/form_view_mixin.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/form/form_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/form/form_model.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/form/setting_view.scss",
            # Graph view
            "/tele_backend_theme_ent/static/src/scss/layout/graph/graph_view.scss",
            # Import view
            "/tele_backend_theme_ent/static/src/scss/layout/import/import_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/import/select_drop.scss",
            #App
            "/tele_backend_theme_ent/static/src/scss/layout/app/expense_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/app/hr_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/app/lunch_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/app/purchase_view.scss",
            #core
            "/tele_backend_theme_ent/static/src/scss/layout/core/loading.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/core/error_message_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/core/nocontent_view.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/core/signout_layout.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/core/effects.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/web_client.scss",
            "/tele_backend_theme_ent/static/src/scss/layout/layout.scss",

            #ent
            "/tele_backend_theme_ent/static/src/scss/ent/secondary_variables.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/control_panel_view.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/dialing_panel.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/chort_view.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/kanban_view.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/referral_view.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/map_view.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/document_veiw.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/barcode_view.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/dashboard_view.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/grid_view.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/form_view.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/gannt_view.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/spreadsheet.scss",
            "/tele_backend_theme_ent/static/src/scss/ent/layout_ent.scss",

            #Responsive
            "/tele_backend_theme_ent/static/src/scss/responsive/home_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/utils.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/chat_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/control_panel_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/left_menu.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/kanban_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/list_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/form_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/configration.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/mail_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/pivot_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/calendar_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/dashboard_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/base_settings.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/spreadsheet.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/r_hr_view.scss",
            "/tele_backend_theme_ent/static/src/scss/responsive/responsive_xs.scss",

            #lib
            "/tele_backend_theme_ent/static/src/lib/custom_radiobutton.scss",
            "/tele_backend_theme_ent/static/src/lib/custom_checkbox.scss",


            #rtl
            "/tele_backend_theme_ent/static/src/scss/rtl/rtl.scss",


            #Night Mode
            "/tele_backend_theme_ent/static/src/scss/night_mode/ni_variables.scss",

            #freamwork
            "/tele_backend_theme_ent/static/src/scss/night_mode/freamwork/ni_control_panel.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/freamwork/ni_header_layout.scss",

            #Views part
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_kanban_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_list_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_graph_layout.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_activity_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_pivot_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_calander_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_mail_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_gernal_setting_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_dashboards_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_form_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_map_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_model_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_import_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_window_chnage_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_grid_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_cohort_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_attendance_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_gantt_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_purchase_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_spreadsheet_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/views/ni_lunch_view.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/ni_common_layout.scss",
            "/tele_backend_theme_ent/static/src/scss/night_mode/ni_layout.scss",

            # <!-- JS Path - start -->
            "/tele_backend_theme_ent/static/src/js/tele_web_themes.js",
            "/tele_backend_theme_ent/static/src/lib/minicolors/jquery.minicolors.min.js",
            "/tele_backend_theme_ent/static/src/js/views/quick_menu.js",
            "/tele_backend_theme_ent/static/src/js/chrome/abstract_action.js",
            "/tele_backend_theme_ent/static/src/js/views/form/form_renderer.js",
            "/tele_backend_theme_ent/static/src/js/views/list/list_model.js",
            "/tele_backend_theme_ent/static/src/js/views/list/list_controller.js",
            "/tele_backend_theme_ent/static/src/js/views/list/list_renderer.js",
            "/tele_backend_theme_ent/static/src/js/views/list/list_view.js",
            "/tele_backend_theme_ent/static/src/js/views/kanban/kanban_controller.js",
            "/tele_backend_theme_ent/static/src/js/views/graph/graph_renderer.js",
            "/tele_backend_theme_ent/static/src/js/freamwork/dashboard.js",
            "/tele_backend_theme_ent/static/src/js/views/import_action.js",
            "/tele_backend_theme_ent/static/src/js/responsive/breadcrumb.js",
            "/tele_backend_theme_ent/static/src/js/views/res_config_settings.js",
            "/tele_backend_theme_ent/static/src/js/views/dialing_panel.js",
            "/tele_backend_theme_ent/static/src/js/components/chat_window/chat_window.js",
            "/tele_backend_theme_ent/static/src/js/components/action_menus.js",
            "/tele_backend_theme_ent/static/src/js/views/control_panel/control_panel.js",
            "/tele_backend_theme_ent/static/src/js/views/control_panel/control_panel_ext.js",
            "/tele_backend_theme_ent/static/src/js/views/control_panel/comparison_menu.js",
            "/tele_backend_theme_ent/static/src/js/views/control_panel/search_bar.js",
            "/tele_backend_theme_ent/static/src/js/core/dialog.js",
            "/tele_backend_theme_ent/static/src/js/main_view.js",
            "/tele_backend_theme_ent/static/src/js/views/menu.js",
            "/tele_backend_theme_ent/static/src/js/chrome/error_handlers.js",
            "/tele_backend_theme_ent/static/src/js/components/dropdown_navigation_hook.js",
            "/tele_backend_theme_ent/static/src/js/components/dropdown_menu.js",
            "/tele_backend_theme_ent/static/src/js/components/dropdown.js",
            "/tele_backend_theme_ent/static/src/js/search/search_panel.js",
            "/tele_backend_theme_ent/static/src/js/search/search_bar/search_bar.js",
            "/tele_backend_theme_ent/static/src/js/webclient/navbar/navbar.js",
            "/tele_backend_theme_ent/static/src/js/webclient/home_menu/home_menu.js",
            "/tele_backend_theme_ent/static/src/js/webclient/navbar/systray_activity_menu.js",
            "/tele_backend_theme_ent/static/src/js/webclient/action_service.js",
            "/tele_backend_theme_ent/static/src/js/webclient/burger_menu.js",
            "/tele_backend_theme_ent/static/src/js/services/systray_hepler.js",
            "/tele_backend_theme_ent/static/src/js/views/graph/color.js",
            "/tele_backend_theme_ent/static/src/js/core/block_ui.js",
            "/tele_backend_theme_ent/static/src/js/fields/basic_fields.js",
            ('remove', '/web_enterprise/static/src/webclient/user_menu.js'),
            ('remove', '/web_enterprise/static/src/webclient/switch_company_menu.js'),
        ],
        'web.assets_backend_prod_only': [
            'tele_backend_theme_ent/static/src/js/main.js',
        ],
        'web.assets_qweb': [
            'tele_backend_theme_ent/static/src/xml/*.xml',
            'tele_backend_theme_ent/static/src/xml/**/*.xml',
        ],
    },
    'post_init_hook': 'post_init_check',
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'auto_install': False,
    'bootstrap': True,
    'application': False,
}
