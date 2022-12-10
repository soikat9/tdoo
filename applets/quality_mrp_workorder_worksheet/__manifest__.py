# -*- encoding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Quality Worksheet for Workorder',
    'version': '1.0',
    'category': 'Manufacturing/Quality',
    'summary': 'Quality Worksheet for Workorder',
    'depends': ['quality_control_worksheet', 'mrp_workorder'],
    'description': """
    Create customizable quality worksheet for workorder.
""",
    "data": [
        'views/mrp_workorder_views.xml',
    ],
    "demo": [
        'data/mrp_workorder_demo.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
