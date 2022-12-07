# -*- encoding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Barcode/Quality/Batch Transfer bridge module",
    'summary': """""",
    'description': """""",
    'category': 'Hidden',
    'version': '1.0',
    'depends': [
        'quality_control_picking_batch',
        'stock_barcode_quality_control',
    ],
    'application': False,
    'auto_install': True,
    'category': 'Hidden',
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'stock_barcode_quality_control_picking_batch/static/**/*',
        ],
    }
}
