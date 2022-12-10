# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Event Barcode in Mobile',
    'category': 'Marketing/Events',
    'summary': 'Event Barcode scan in Mobile',
    'version': '1.0',
    'description': """ """,
    'depends': ['event_barcode', 'barcodes_mobile'],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'event_barcode_mobile/static/src/js/**/*',
        ],
        'web.assets_qweb': [
            'event_barcode_mobile/static/src/xml/**/*',
        ],
    }
}
