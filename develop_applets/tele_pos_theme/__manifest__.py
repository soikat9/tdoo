# -*- coding: utf-8 -*-

{
    "name": "POS Theme",
    "version":"1.0.1",
    "license": "TPL-1",
    "category": "Point of Sale",     
    "summary": "Pos theme, point of sale",
    "description": """

    """,
    "depends": [
        "point_of_sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        'views/pos_theme.xml',
        "data/pos_theme_data.xml",
    ],

    "assets": {
        "point_of_sale.assets": [
            '/tele_pos_theme/static/src/scss/pos_theme_variables.scss',    
            '/tele_pos_theme/static/src/scss/theme.scss',                                              
        ]
    },
    "images": ["",],              
    "installable": True,
    "application": True,
    "auto_install": False,
}
