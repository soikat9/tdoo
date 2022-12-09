# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Gauge Widget for Kanban',
    'category': 'Hidden',
    'description': """
This widget allows to display gauges using d3 library.
""",
    'version': '1.0',
    'depends': ['web'],
    'assets' : {
        'web.assets_backend': [
            'web_kanban_gauge/static/src/**/*',
        ],
        'web.qunit_suite_tests': [
            'web_kanban_gauge/static/tests/**/*',
        ],
    },
    'auto_install': True,
    'license': 'LGPL-3',
}
