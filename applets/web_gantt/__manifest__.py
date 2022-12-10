# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Web Gantt',
    'category': 'Hidden',
    'description': """
Tele Web Gantt chart view.
=============================

    """,
    'version': '2.0',
    'depends': ['web'],
    'assets': {
        'web.assets_qweb': [
            'web_gantt/static/src/xml/**/*',
        ],
        'web.assets_backend': [
            'web_gantt/static/src/**/*',
        ],
        'web.qunit_suite_tests': [
            'web_gantt/static/tests/**/*',
        ],
    },
    'auto_install': True,
    'license': 'TEEL-1',
}
