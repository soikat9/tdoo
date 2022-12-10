# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Time Off in Payslips Enterprise',
    'version': '1.0',
    'category': 'Human Resources/Payroll',
    'sequence': 95,
    'summary': 'Manage Time Off in Payslips Enterprise',
    'description': """
Manage Time Off in Payslips
============================

This application allows you to integrate time off in payslips.
    """,
    'depends': ['hr_work_entry_holidays'],
    'data': [
        'views/hr_work_entry_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'TEEL-1',
}
