# -*- coding: utf-8 -*-
{
	'name': 'Dashboard Workspace',

	'summary': """

""",

	'description': """

""",

	'license': 'TPL-1',

	'category': 'Tools',

	'version': '1.0.1.1.8',

	'depends': ['base', 'web', 'base_setup', 'bus'],

	'data': ['security/ir.model.access.csv', 'security/tele_security_groups.xml', 'data/tele_default_data.xml', 'views/tele_dashboard_workspace_view.xml', 'views/tele_dashboard_workspace_item_view.xml', 'views/tele_dashboard_action.xml', 'views/tele_import_dashboard_view.xml', 'wizard/tele_create_dashboard_wiz_view.xml', 'wizard/tele_duplicate_dashboard_wiz_view.xml'],

	'demo': ['demo/tele_dashboard_workspace_demo.xml'],

	'assets': {'web.assets_backend': ['tele_dashboard_workspace/static/src/css/tele_dashboard_workspace.scss', 'tele_dashboard_workspace/static/src/css/tele_dashboard_workspace_item.css', 'tele_dashboard_workspace/static/src/css/tele_icon_container_modal.css', 'tele_dashboard_workspace/static/src/css/tele_dashboard_item_theme.css', 'tele_dashboard_workspace/static/src/css/tele_dn_filter.css', 'tele_dashboard_workspace/static/src/css/tele_toggle_icon.css', 'tele_dashboard_workspace/static/src/css/tele_dashboard_options.css', 'tele_dashboard_workspace/static/src/js/tele_global_functions.js', 'tele_dashboard_workspace/static/src/js/tele_dashboard_workspace.js', 'tele_dashboard_workspace/static/src/js/tele_to_do_dashboard.js', 'tele_dashboard_workspace/static/src/js/tele_filter_props.js', 'tele_dashboard_workspace/static/src/js/tele_color_picker.js', 'tele_dashboard_workspace/static/src/js/tele_dashboard_workspace_item_preview.js', 'tele_dashboard_workspace/static/src/js/tele_image_basic_widget.js', 'tele_dashboard_workspace/static/src/js/tele_dashboard_item_theme.js', 'tele_dashboard_workspace/static/src/js/tele_widget_toggle.js', 'tele_dashboard_workspace/static/src/js/tele_import_dashboard.js', 'tele_dashboard_workspace/static/src/js/tele_domain_fix.js', 'tele_dashboard_workspace/static/src/js/tele_quick_edit_view.js', 'tele_dashboard_workspace/static/src/js/tele_dashboard_workspace_kpi_preview.js', 'tele_dashboard_workspace/static/src/js/tele_date_picker.js', 'tele_dashboard_workspace/static/lib/css/gridstack.min.css', 'tele_dashboard_workspace/static/lib/js/gridstack-h5.js', 'tele_dashboard_workspace/static/lib/js/Chart.bundle.min.js', 'tele_dashboard_workspace/static/src/css/tele_dashboard_workspace_pro.css', 'tele_dashboard_workspace/static/src/css/tele_to_do_item.css', 'tele_dashboard_workspace/static/src/js/tele_dashboard_workspace_graph_preview.js', 'tele_dashboard_workspace/static/src/js/tele_dashboard_workspace_list_view_preview.js', 'tele_dashboard_workspace/static/src/js/tele_to_do_preview.js'], 'web.assets_qweb': ['tele_dashboard_workspace/static/src/xml/**/*']},

	'uninstall_hook': 'uninstall_hook',
}
