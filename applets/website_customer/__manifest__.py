# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Customer References',
    'category': 'Website/Website',
    'summary': 'Publish your customer references',
    'version': '1.0',
    'description': """
Publish your customers as business references on your website to attract new potential prospects.
    """,
    'depends': [
        'website_crm_partner_assign',
        'website_partner',
        'website_google_map',
    ],
    'demo': [
        'data/res_partner_demo.xml',
    ],
    'data': [
        'views/website_customer_templates.xml',
        'views/res_partner_views.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
