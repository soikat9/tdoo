# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Marketing Automation Tests",
    'version': "1.1",
    'summary': "Test Suite for Automated Marketing Campaigns",
    'category': "Hidden",
    'depends': [
        'marketing_automation',
        'marketing_automation_sms',
        'test_mail',
        'test_mail_enterprise',
        'test_mail_full',
        'test_mass_mailing',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'application': False,
    'license': 'TEEL-1',
}
