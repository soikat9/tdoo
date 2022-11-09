# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    "name": "TaxCloud and Subscriptions",
    "summary": """Compute taxes with TaxCloud after automatic invoice creation.""",
    "description": """This module ensures that the taxes are computed on the invoice before a payment is created automatically for a subscription.
    """,
    "category": 'Sales/Subscriptions',
    "depends": ["sale_subscription", "account_taxcloud"],
    "auto_install": True,
    "license": "TEEL-1",
}
