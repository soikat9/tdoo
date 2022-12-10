# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Subscription and Timesheet',
    'summary': 'Synchronize data between timesheet and subscriptions',
    'description': """This module ensure that data (such as analytic accounts) defined on the sale order via timesheet app are correctly set also on subscriptions""",
    'category': 'Sales/Subscription',
    'depends': [
        'sale_subscription',
        'sale_timesheet',
    ],
    'auto_install': True,
    'license': 'TEEL-1',
}
