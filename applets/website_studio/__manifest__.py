# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    'name': "Website Studio",
    'summary': "Display Website Elements in Studio",
    'description': """
Studio - Customize Tele
=======================

This applet allows the user to display all the website forms linked to a certain
model. Furthermore, you can create a new website form or edit an existing one.

""",
    'category': 'Hidden',
    'version': '1.0',
    'depends': [
        'tele_studio',
        'website',
    ],
    'data': [
        'views/templates.xml',
        'views/actions.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
    'assets': {
        'tele_studio.studio_assets': [
            'website_studio/static/src/js/**/*.js',
            'website_studio/static/src/scss/**/*.scss',
        ],
        'web.assets_qweb': [
            'website_studio/static/src/xml/*.xml',
        ],
        'web.qunit_suite_tests': [
            'website_studio/static/tests/**/*',
        ],
    }
}
