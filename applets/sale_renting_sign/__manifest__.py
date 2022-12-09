# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
{
    "name": "Rental/Sign Bridge",
    "summary": """
            Bridge Sign functionalities with the Rental application
        """,
    "author": "Tele INC.",
    "website": "https://www.tele.studio",
    "category": "Sales/Sales",
    "version": "1.0",
    "depends": ["sign", "sale_renting"],
    "data": [
        "security/ir.model.access.csv",
        "security/rental_sign_security.xml",
        "wizard/rental_sign_views.xml",
        "data/mail_templates.xml",
        "views/res_config_settings_views.xml",
        "views/sale_rental_views.xml",
    ],
    "demo": [
        "data/demo.xml",
    ],
    "auto_install": False,
    'license': 'TEEL-1',
}
