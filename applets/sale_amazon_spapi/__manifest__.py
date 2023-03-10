# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    'name': "Amazon/Selling Partner API Patch",
    'summary': "Patch module to migrate to the Selling Partner API",
    'description': """
This module migrates the Amazon Connector from the MWS API to the Selling Partner API.
""",
    'category': 'Sales/Sales',
    'version': '1.0',
    'depends': ['sale_amazon'],
    'application': False,
    'auto_install': True,
    'data': [
        'data/amazon_data.xml',

        'views/amazon_account_views.xml',
        'views/amazon_marketplace_views.xml',
        'views/amazon_templates.xml',
    ],
    'license': 'TEEL-1',
}
