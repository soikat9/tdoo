# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Cohort View',
    'summary': 'Basic Cohort view for tele',
    'description': """
    """,
    'category': 'Hidden',
    'depends': ['web'],
    'assets': {
        'web.assets_qweb': [
            'web_cohort/static/src/**/*.xml',
        ],
        'web.assets_backend': [
            'web_cohort/static/src/**/*',
            ("remove", "web_cohort/static/src/legacy/**/*"),
        ],
        "web.assets_backend_legacy_lazy": [
            "web_cohort/static/src/legacy/**/*.js",
        ],
        'web.qunit_suite_tests': [
            'web_cohort/static/tests/**/*.js',
        ],
    },
    'auto_install': True,
    'license': 'TEEL-1',
}
