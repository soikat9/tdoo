# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.depends('order_line.move_dest_ids.group_id.sale_id', 'order_line.move_ids.move_dest_ids.group_id.sale_id')
    def _compute_sale_order_count(self):
        super(PurchaseOrder, self)._compute_sale_order_count()

    def _get_sale_orders(self):
        return super(PurchaseOrder, self)._get_sale_orders() | self.order_line.move_dest_ids.group_id.sale_id | self.order_line.move_ids.move_dest_ids.group_id.sale_id
