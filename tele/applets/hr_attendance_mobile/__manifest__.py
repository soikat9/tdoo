# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Attendances Barcode in Mobile',
    'category': 'Human Resources/Attendances',
    'summary': 'Attendances Barcode scan in Mobile',
    'version': '1.0',
    'description': """ """,
    'depends': ['hr_attendance', 'barcodes_mobile'],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'hr_attendance_mobile/static/src/js/**/*',
        ],
        'web.assets_qweb': [
            'hr_attendance_mobile/static/src/xml/**/*',
        ],
    }
}