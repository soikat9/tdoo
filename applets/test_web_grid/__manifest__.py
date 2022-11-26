# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Web Grid Tests',
    'version': '1.0',
    'category': 'Hidden',
    'summary': 'Web Grid Tests: performances and tests specific to the grid view',
    'description': """This module contains tests related to the web grid view. Those are
present in a separate module as it contains models used only to perform
tests independently to functional aspects of other models. """,
    'depends': ['web_grid'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'license': 'TEEL-1',
}
