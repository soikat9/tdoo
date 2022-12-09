# -*- encoding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Project Time Off",
    'version': '1.0',
    'category': 'Hidden',
    'summary': "Project and task integration with holidays",
    'description': """
Project and task integration with holidays
    """,
    'depends': ['project_enterprise', 'hr_holidays_gantt'],
    'data': [
        'views/project_task_views.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
