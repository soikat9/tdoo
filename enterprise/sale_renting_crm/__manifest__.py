# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Opportunity to Rental',
    'version': '1.0',
    'category': 'Hidden',
    'description': """
This module adds a shortcut on one or several opportunity cases in the CRM.
===========================================================================

This shortcut allows you to generate a rental order based on the selected case.
    """,
    'depends': ['sale_renting', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'wizard/crm_lead_rental_views.xml',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
