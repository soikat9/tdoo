# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields
from tele.tools.translate import _


class BarcodeRule(models.Model):
    _inherit = 'barcode.rule'

    type = fields.Selection(selection_add=[
        ('weight', 'Weighted Product'),
        ('price', 'Priced Product'),
        ('discount', 'Discounted Product'),
        ('client', 'Client'),
        ('cashier', 'Cashier')
    ], ondelete={
        'weight': 'set default',
        'price': 'set default',
        'discount': 'set default',
        'client': 'set default',
        'cashier': 'set default',
    })
