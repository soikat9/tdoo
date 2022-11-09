# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Contact Form',
    'category': 'Website/Website',
    'sequence': 54,
    'summary': 'Generate leads from a contact form',
    'version': '2.1',
    'description': """
Add capability to your website forms to generate leads or opportunities in the CRM app.
Forms has to be customized inside the *Website Builder* in order to generate leads.

This module includes contact phone and mobile numbers validation.""",
    'depends': ['website', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_actions_data.xml',
        'data/ir_model_data.xml',
        'views/crm_lead_views.xml',
        'views/res_config_settings_views.xml',
        'views/website_visitor_views.xml',
        'views/website_templates_contactus.xml',
    ],
    'installable': True,
    'auto_install': True,
    'assets': {
        'website.assets_editor': [
            'website_crm/static/src/**/*',
        ],
        'web.assets_tests': [
            'website_crm/static/tests/**/*',
        ],
    },
    'license': 'LGPL-3',
}
