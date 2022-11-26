{
    'name': 'Tele Studio for Community',
    'summary': 'Tele Studio for Community',
    'version': '1.0',
    'category': 'Web',
    'description': """
        Tele Studio. Build and Customize Tele Apps on the fly without any technical knowledge.
    """,
    'author': "apps.tele.community@gmail.com",
    "website": "tele-studio.com",
    'depends': ['base_automation'],
    'data': [
        'views/menu_view.xml',
        'views/action_studio_view.xml',
        'views/report_kanban_view.xml',
        'security/view_dynamic_security.xml',
        'security/ir.model.access.csv',

    ],
    'assets': {
        'web.assets_qweb': [
            '/dynamic_tele/static/src/xml/report_center.xml',
            '/dynamic_tele/static/src/xml/views.xml',
            '/dynamic_tele/static/src/xml/widgets.xml',
            '/dynamic_tele/static/src/xml/base.xml',
            '/dynamic_tele/static/src/xml/menu.xml',
            '/dynamic_tele/static/src/xml/icons.xml',
            '/dynamic_tele/static/src/xml/fields.xml',
            '/dynamic_tele/static/src/xml/gantt_view.xml',
            '/dynamic_tele/static/src/xml/planning_view.xml',
            '/dynamic_tele/static/src/xml/form_components.xml',
            '/dynamic_tele/static/src/xml/kanban_view.xml',
            '/dynamic_tele/static/src/xml/dashboard_view.xml',
            '/dynamic_tele/static/src/xml/components.xml',
            '/dynamic_tele/static/src/js/base/navbar/navbar.xml',
        ],
        "web.report_assets_common": [
            "/dynamic_tele/static/src/scss/studio_report.scss",
        ],
        'web.assets_backend': [
            "/dynamic_tele/static/src/scss/base.scss",
            "/dynamic_tele/static/src/scss/automation_access.scss",
            "/dynamic_tele/static/src/scss/views.scss",
            "/dynamic_tele/static/src/scss/fields.scss",
            "/dynamic_tele/static/src/scss/widgets.scss",
            "/dynamic_tele/static/src/scss/planning_view.scss",
            "/dynamic_tele/static/src/scss/form_components.scss",
            "/dynamic_tele/static/src/scss/menu_edit.scss",
            "/dynamic_tele/static/src/scss/report_center.scss",
            # "/dynamic_tele/static/src/scss/form_center.scss",
            "/dynamic_tele/static/src/js/base/navbar/navbar.scss",
            "/dynamic_tele/static/src/lib/gridstackjs/gridstack.min.css",
            "/dynamic_tele/static/src/lib/gridstackjs/gridstack-h5.min.js",
            "/dynamic_tele/static/src/lib/dom_to_image.min.js",
            "/dynamic_tele/static/src/lib/jspdf.min.js",
            "/dynamic_tele/static/src/js/libs/jquery.js",
            # "/dynamic_tele/static/src/js/chrome/abstract_web_client.js",
            # "/dynamic_tele/static/src/js/chrome/action_manager.js",
            "/dynamic_tele/static/src/js/base/fields/tele_base_fields.js",
            "/dynamic_tele/static/src/js/base/navbar/navbar.js",
            "/dynamic_tele/static/src/js/base/services/menu_service.js",
            "/dynamic_tele/static/src/js/base/services/view_service.js",
            "/dynamic_tele/static/src/js/base/views/form_view/form_controller.js",
            "/dynamic_tele/static/src/js/base/views/form_view/form_renderer.js",
            "/dynamic_tele/static/src/js/base/views/graph_view/graph_view.js",
            "/dynamic_tele/static/src/js/base/views/list_view/list_renderer.js",
            "/dynamic_tele/static/src/js/base/views/planning_view/planning_controller.js",
            "/dynamic_tele/static/src/js/base/views/planning_view/planning_model.js",
            "/dynamic_tele/static/src/js/base/views/planning_view/planning_renderer.js",
            "/dynamic_tele/static/src/js/base/views/planning_view/planning_view.js",
            "/dynamic_tele/static/src/js/base/views/basic_model.js",
            "/dynamic_tele/static/src/js/base/widgets/widgets.js",

            "/dynamic_tele/static/src/js/studio/base/base.js",
            "/dynamic_tele/static/src/js/studio/base/basic_fields.js",
            "/dynamic_tele/static/src/js/studio/base/basic_widgets.js",
            "/dynamic_tele/static/src/js/studio/base/view_container.js",
            "/dynamic_tele/static/src/js/studio/base/views_edit_base.js",
            "/dynamic_tele/static/src/js/studio/menus/menu_center.js",
            "/dynamic_tele/static/src/js/studio/menus/systray_menu_studio.js",
            "/dynamic_tele/static/src/js/studio/other/view_tree_form.js",
            "/dynamic_tele/static/src/js/studio/reports/ReportCenter.js",
            "/dynamic_tele/static/src/js/studio/reports/ReportEdit.js",
            "/dynamic_tele/static/src/js/studio/reports/ReportKanBan.js",
            "/dynamic_tele/static/src/js/studio/views/activity.js",
            "/dynamic_tele/static/src/js/studio/views/basic.js",
            "/dynamic_tele/static/src/js/studio/views/calendar.js",
            "/dynamic_tele/static/src/js/studio/views/form.js",
            "/dynamic_tele/static/src/js/studio/views/graph.js",
            "/dynamic_tele/static/src/js/studio/views/pivot.js",
            "/dynamic_tele/static/src/js/studio/views/kanban.js",
            "/dynamic_tele/static/src/js/studio/views/planning.js",
            "/dynamic_tele/static/src/js/studio/views/search.js",
            "/dynamic_tele/static/src/js/studio/views/tree.js",

            "/dynamic_tele/static/src/js/studio/app_center.js",
            "/dynamic_tele/static/src/js/studio/base_center.js",
            # "/dynamic_tele/static/src/js/studio/menu_center.js",
            "/dynamic_tele/static/src/js/studio/views_center.js",
            "/dynamic_tele/static/src/js/start.js",
        ],
    },
    'images': ['images/main_screen.jpg'],
    'license': 'TPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
    'images': [
        'static/description/module_image.jpg',
    ],
}
