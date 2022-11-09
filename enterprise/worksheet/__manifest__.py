# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Worksheet',
    'category': 'Hidden',
    'summary': 'Create customizable worksheet',
    'description': """
Create customizable worksheet
================================

""",
    'depends': ['tele_studio'],
    'data': [
        'security/ir.model.access.csv',
        'security/worksheet_security.xml',
        'views/worksheet_template_view.xml',
    ],
    'demo': [],
    'assets': {
        'web.assets_backend': [
            'worksheet/static/**/*',
        ],
    },
    'license': 'TEEL-1',
}
