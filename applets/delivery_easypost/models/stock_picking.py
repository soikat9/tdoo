# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    ep_order_ref = fields.Char("Easypost Order Reference", copy=False)
