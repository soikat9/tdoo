# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class Attachment(models.Model):

    _inherit = ['ir.attachment']

    product_downloadable = fields.Boolean("Downloadable from product portal", default=False)
