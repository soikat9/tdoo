# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class Product(models.Model):
    _inherit = "product.product"

    channel_ids = fields.One2many('slide.channel', 'product_id', string='Courses')
