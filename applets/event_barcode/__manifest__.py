# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Event Barcode Scanning",
    'summary': "Add barcode scanning feature to event management.",
    'version': '1.0',
    'description': """
This module adds support for barcodes scanning to the Event management system.
A barcode is generated for each attendee and printed on the badge. When scanned,
the registration is confirmed.
    """,
    'category': 'Marketing/Events',
    'depends': ['barcodes', 'event'],
    'data': [
        'views/event_event_views.xml',
        'views/event_registration_views.xml',
        'views/event_report_templates.xml',
        'views/res_config_settings_views.xml',
    ],
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'event_barcode/static/src/js/event_barcode.js',
            'event_barcode/static/src/scss/event_barcode.scss',
        ],
        'web.assets_qweb': [
            'event_barcode/static/src/xml/**/*',
        ],
        'web.report_assets_common': [
            '/event_barcode/static/src/scss/event_foldable_badge_report.scss',
            '/event_barcode/static/src/scss/event_full_page_ticket_report.scss',
        ],
    }
}
