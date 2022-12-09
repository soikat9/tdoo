# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Accounting - MRP',
    'version': '1.0',
    'category': 'Manufacturing/Manufacturing',
    'summary': 'Analytic accounting in Manufacturing',
    'description': """
Analytic Accounting in MRP
==========================

* Cost structure report
""",
    'website': 'https://www.tele.studio/app/manufacturing',
    'depends': ['mrp_account'],
    'data': [
        'security/ir.model.access.csv',
        'security/mrp_account_enterprise_security.xml',
        'views/mrp_account_view.xml',
        'views/cost_structure_report.xml',
        'reports/mrp_report_views.xml',
        ],
    'demo': ['demo/mrp_account_demo.xml'],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_common': [
            'mrp_account_enterprise/static/**/*',
        ],
    }
}
