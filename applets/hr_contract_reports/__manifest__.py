# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Employee Contracts Reporting',
    'version': '1.0',
    'category': 'Human Resources/Contracts',
    'description': """
Add a dynamic report about contracts and employees.
    """,
    'website': 'https://www.tele.studio/app/employees',
    'depends': ['hr_contract', 'web_dashboard'],
    'data': [
        'security/ir.model.access.csv',
        'report/hr_contract_employee_report_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
