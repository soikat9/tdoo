
# -*- encoding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Quality Base',
    'version': '1.0',
    'category': 'Manufacturing/Quality',
    'sequence': 50,
    'summary': 'Basic Feature for Quality',
    'depends': ['stock'],
    'description': """
Quality Base
===============
* Define quality points that will generate quality checks on pickings,
  manufacturing orders or work orders (quality_mrp)
* Quality alerts can be created independently or related to quality checks
* Possibility to add a measure to the quality check with a min/max tolerance
* Define your stages for the quality alerts
""",
    'data': [
        'security/quality.xml',
        'security/ir.model.access.csv',
        'data/quality_data.xml',
        'views/quality_views.xml',
    ],
    'demo': [],
    'application': False,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'quality/static/src/js/tablet_image_widget.js',
            'quality/static/src/scss/tablet_view.scss',
        ],
        'web.assets_qweb': [
            'quality/static/src/xml/**/*',
        ],
    }
}
