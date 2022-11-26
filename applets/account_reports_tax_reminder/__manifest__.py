# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name' : 'Accounting Reports Tax Reminder',
    'summary': 'Add a notification when the tax report has been generated',
    'category': 'Accounting/Accounting',
    'description': """
Accounting Reports Tax Reminder
===============================
This module adds a notification when the tax report is ready to be sent
to the administration.
    """,
    'depends': ['account_reports'],
    'data': [
        'data/account_reports_tax_reminder.xml',
    ],
    'auto_install': True,
    'installable': True,
    'license': 'TEEL-1',
}
