# -*- encoding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'MRP features for Quality Control with IoT',
    'summary': 'Quality Management with MRP and IoT',
    'depends': ['quality_mrp_workorder', 'iot'],
    'category': 'Manufacturing/Quality',
    'description': """
    Adds Quality Control to workorders with IoT.
""",
    "data": [
        'views/mrp_workorder_views.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
