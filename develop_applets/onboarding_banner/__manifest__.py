# -*- coding: utf-8 -*-
{
    'name': "onboarding_banner",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.tele.studio""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Tele INC",
    'website': "http://www.tele.studio",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
