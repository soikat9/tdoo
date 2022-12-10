# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Lead Generation From Website Visits',
    'summary': 'Generate Leads/Opportunities from your website\'s traffic',
    'version': '1.1',
    'category': 'Sales/CRM',
    'depends': [
        'iap_crm',
        'iap_mail',
        'crm_iap_mine',
        'website'
    ],
    'data': [
        'data/ir_cron_data.xml',
        'data/ir_model_data.xml',
        'security/ir_rules.xml',
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/crm_reveal_views.xml',
        'views/res_config_settings_views.xml',
        'views/crm_menus.xml',
    ],
    'license': 'LGPL-3',
}
