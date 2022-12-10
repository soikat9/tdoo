#-*- coding:utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': 'Payroll Accounting',
    'category': 'Human Resources/Payroll',
    'description': """
Generic Payroll system Integrated with Accounting.
==================================================

    * Expense Encoding
    * Payment Encoding
    * Company Contribution Management
    """,
    'depends': ['hr_payroll', 'account_accountant'],
    'data': [
        'views/hr_payroll_account_views.xml',
        'report/hr_contract_history_report_views.xml'],
    'demo': ['data/hr_payroll_account_demo.xml'],
    'auto_install': True,
    'license': 'TEEL-1',
}
