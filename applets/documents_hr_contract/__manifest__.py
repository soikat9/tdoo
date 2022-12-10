# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Documents - Contracts',
    'version': '1.0',
    'category': 'Productivity/Documents',
    'summary': 'Store employee contracts in the Document app',
    'description': """
Employee contracts files will be automatically integrated to the Document app.
""",
    'website': ' ',
    'depends': ['documents_hr', 'hr_contract'],
    'data': ['data/data.xml', 'views/documents_views.xml'],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
}
