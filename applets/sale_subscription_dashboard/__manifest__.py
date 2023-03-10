# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': 'Sale Subscription Dashboard',
    'version': '1.0',
    'depends': ['sale_subscription'],
    'description': """
Sale Subscription Dashboard
===========================
It adds dashboards to :
1) Analyse the recurrent revenue and other metrics for subscriptions
2) Analyse the subscriptions modifications by salesman and compute their value.
    """,
    'website': 'https://www.tele.studio/app/accounting',
    'category': 'Sales/Subscriptions',
    'data': [
        'views/sale_subscription_dashboard_views.xml',
        'views/report_dashboard.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': True,
    'license': 'TEEL-1',
    'assets': {
        'web.assets_backend': [
            'sale_subscription_dashboard/static/src/scss/sale_subscription_dashboard.scss',
            'sale_subscription_dashboard/static/src/js/sale_subscription_dashboard.js',
            'sale_subscription_dashboard/static/src/js/action_sale_subscription_dashboard_dl.js',
        ],
        'web.qunit_suite_tests': [
            'sale_subscription_dashboard/static/tests/**/*',
        ],
        'web.assets_qweb': [
            'sale_subscription_dashboard/static/src/xml/**/*',
        ],
    }
}
