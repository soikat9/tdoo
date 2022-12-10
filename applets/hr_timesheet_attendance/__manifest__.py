# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Timesheets/attendances reporting",
    'description': """
    Module linking the attendance module to the timesheet app.
    """,
    'category': 'Hidden',
    'version': '1.0',

    'depends': ['hr_timesheet', 'hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_timesheet_attendance_report_security.xml',
        'report/hr_timesheet_attendance_report_view.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
