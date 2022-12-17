# -*- coding: utf-8 -*-
# Part of Tele. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    'name': 'Tele Backend Theme Enterprise Studio',
    'category': "Themes/Backend",
    'version': '1.0',
    'license': 'TPL-1',
    'summary': 'Customized Backend Theme With studio',
    'description': 'Customized Backend Theme With studio',
    'depends': ['tele_studio','tele_backend_theme_ent'],
    'assets': {
        'web.assets_backend': [
            '/tele_studio_ent/static/src/scss/ent/studio_form.scss',
            '/tele_studio_ent/static/src/scss/ent/studio_list.scss',
            '/tele_studio_ent/static/src/scss/ent/studio_kanban.scss',
            '/tele_studio_ent/static/src/scss/ent/studio_calendar.scss',
            '/tele_studio_ent/static/src/scss/ent/studio_pivot.scss',
            '/tele_studio_ent/static/src/scss/ent/studio_graph.scss',
            '/tele_studio_ent/static/src/scss/ent/studio_cohort.scss',
            '/tele_studio_ent/static/src/scss/ent/studio_gannt.scss',
            '/tele_studio_ent/static/src/scss/ent/studio_grid.scss',
            '/tele_studio_ent/static/src/scss/ent/layout_ent.scss',
            '/tele_studio_ent/static/src/scss/responsive/left_menu.scss',
            '/tele_studio_ent/static/src/scss/responsive/responsive-xs.scss',
            '/tele_studio_ent/static/src/scss/responsive/layout.scss',
        ],
        'tele_studio.studio_assets': [
            '/tele_studio_ent/static/src/js/views/view_editors/form_editor.js',
        ],
    },
    'images': [
        '',
        '',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}