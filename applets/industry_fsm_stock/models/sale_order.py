# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line']

    fsm_lot_id = fields.Many2one('stock.production.lot', domain="[('product_id', '=', product_id)]")
