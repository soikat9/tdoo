# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Resource',
    'version': '1.1',
    'category': 'Hidden',
    'description': """
Module for resource management.
===============================

A resource represent something that can be scheduled (a developer on a task or a
work center on manufacturing orders). This module manages a resource calendar
associated to every resource. It also manages the leaves of every resource.
    """,
    'depends': ['base', 'web'],
    'data': [
        'data/resource_data.xml',
        'security/ir.model.access.csv',
        'security/resource_security.xml',
        'views/resource_views.xml',
        ],
    'demo': [
    ],
    'assets': {
        'web.assets_backend': [
            'resource/static/**/*',
        ],
    },
    'license': 'LGPL-3',
}
