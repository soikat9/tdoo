# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


class BarcodeRule(models.Model):
    _inherit = 'barcode.rule'

    type = fields.Selection(selection_add=[
        ('gift_card', 'Gift Card'),
    ], ondelete={
        'gift_card': 'set default',
    })
