# -*- coding: utf-8 -*-

{
    "name": "Backend Theme",
    "summary": "Backend theme, Responsive theme, Fullu customizable theme, Material backend theme",
    "version": "1.0.1",
    "category": "Themes/Backend",
    "license": "TPL-1", 
    "depends": ["web", "mail"],   
    "data": [
        "views/res_users.xml", 
        "views/web.xml",
        "views/alpha_theme_setting.xml",
        "security/ir.model.access.csv",
        "data/alpha_theme_data.xml",
        ],
    "assets": {
        "web.assets_frontend": [
            "/rt_alpha_backend_theme/static/src/legacy/js/website_apps_menu.js",
            "/rt_alpha_backend_theme/static/src/legacy/scss/website_apps_menu.scss",
            "/rt_alpha_backend_theme/static/src/scss/login.scss",
        ],
        "web.assets_backend": [
            "/rt_alpha_backend_theme/static/src/scss/alpha_theme_variables.scss",             
            "/rt_alpha_backend_theme/static/src/legacy/scss/rt_alpha_backend_theme.scss",
            "/rt_alpha_backend_theme/static/src/legacy/js/rt_alpha_backend_theme.js",
            "/rt_alpha_backend_theme/static/src/legacy/scss/kanban_view_mobile.scss",
            "/rt_alpha_backend_theme/static/src/legacy/js/kanban_renderer_mobile.js",
            "/rt_alpha_backend_theme/static/src/components/ui_context.esm.js",
            "/rt_alpha_backend_theme/static/src/components/apps_menu/apps_menu.scss",
            "/rt_alpha_backend_theme/static/src/components/apps_menu/apps_menu.esm.js",
            "/rt_alpha_backend_theme/static/src/components/navbar/main_navbar.scss",
            "/rt_alpha_backend_theme/static/src/components/control_panel/control_panel.scss",
            "/rt_alpha_backend_theme/static/src/components/control_panel/control_panel.esm.js",
            "/rt_alpha_backend_theme/static/src/components/search_panel/search_panel.scss",
            "/rt_alpha_backend_theme/static/src/components/search_panel/search_panel.esm.js",
            "/rt_alpha_backend_theme/static/src/components/attachment_viewer/attachment_viewer.scss",
            "/rt_alpha_backend_theme/static/src/components/attachment_viewer/attachment_viewer.esm.js",
            "/rt_alpha_backend_theme/static/src/components/hotkey/hotkey.scss",
            "/rt_alpha_backend_theme/static/src/scss/alpha_setting.scss",
            "/rt_alpha_backend_theme/static/src/scss/style.scss",
            "/rt_alpha_backend_theme/static/src/scss/dark_mode.scss",
            "/rt_alpha_backend_theme/static/src/js/systray/systray_dark_mode_menu.js", 
        ],
        "web.assets_qweb": [
            "/rt_alpha_backend_theme/static/src/xml/dark_mode.xml",
            "/rt_alpha_backend_theme/static/src/legacy/xml/form_buttons.xml",
            "/rt_alpha_backend_theme/static/src/components/apps_menu/apps_menu.xml",
            "/rt_alpha_backend_theme/static/src/components/control_panel/control_panel.xml",
            "/rt_alpha_backend_theme/static/src/components/navbar/main_navbar.xml",
            "/rt_alpha_backend_theme/static/src/components/search_panel/search_panel.xml",
            "/rt_alpha_backend_theme/static/src/components/attachment_viewer/attachment_viewer.xml",
            "/rt_alpha_backend_theme/static/src/components/hotkey/hotkey.xml",    
            "/rt_alpha_backend_theme/static/src/xml/systray_dark_mode_menu.xml",
            "/rt_alpha_backend_theme/static/src/xml/pivot_view_inherit.xml",
        ],
    
    'installable': True,
    'application': False,
    'auto_install': False,

}
}
