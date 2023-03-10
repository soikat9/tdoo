# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Compare timesheets and forecast for your projects',
    'version': '1.0',
    'category': 'Services/Project',
    'description': """
Compare timesheets and forecast for your projects.
==================================================

In your project plan, you can compare your timesheets and your forecast to better schedule your resources.
    """,
    'website': 'https://www.tele.studio/app/project',
    'depends': ['project_timesheet_forecast', 'sale_timesheet', 'sale_project_forecast'],
    'data': [
        'report/timesheet_forecast_report_views.xml',
        'views/project_project_views.xml',
        'views/project_update_templates.xml',
    ],
    'demo': [
        'data/product_demo.xml',
        'data/forecast_demo.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
