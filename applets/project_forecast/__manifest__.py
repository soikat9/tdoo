# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': "Project Planning",
    'summary': """Plan your resources on project tasks""",
    'description': """
    Schedule your teams across projects and estimate deadlines more accurately.
    """,
    'category': 'Services/Project',
    'version': '1.0',
    'depends': ['project', 'planning', 'web_grid'],
    'data': [
        'views/planning_template_views.xml',
        'views/planning_templates.xml',
        'views/planning_views.xml',
        'views/project_forecast_views.xml',
        'views/project_views.xml',
    ],
    'application': False,
    'license': 'TEEL-1',
    'post_init_hook': 'post_init',
    'uninstall_hook': '_uninstall_hook',
    'assets': {
        'web.assets_backend': [
            'project_forecast/static/src/js/forecast_gantt.js',
        ],
        'web.assets_frontend': [
            'project_forecast/static/src/js/forecast_calendar_front.js',
        ],
    }
}
