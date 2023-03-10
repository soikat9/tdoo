# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Recruitment Reporting',
    'version': '1.0',
    'category': 'Human Resources/Recruitment',
    'description': """
Add a dynamic report about recruitment.
    """,
    'website': 'https://www.tele.studio/app/recruitment',
    'depends': ['hr_recruitment', 'web_dashboard'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_recruitment_reports_security.xml',
        'report/hr_recruitment_report_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
