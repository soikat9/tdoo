# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Documents - Payroll',
    'version': '1.0',
    'category': 'Productivity/Documents',
    'summary': 'Store employee payslips in the Document app',
    'description': """
Employee payslips will be automatically integrated to the Document app.
""",
    'website': ' ',
    'depends': ['documents_hr', 'hr_payroll'],
    'data': [
        'data/data.xml',
        'views/documents_views.xml',
        'security/security.xml'
    ],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
