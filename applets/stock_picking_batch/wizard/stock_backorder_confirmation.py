# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class StockBackorderConfirmation(models.TransientModel):
    _inherit = 'stock.backorder.confirmation'

    def process(self):
        res = super().process()
        if self.env.context.get('pickings_to_detach'):
            self.env['stock.picking'].browse(self.env.context['pickings_to_detach']).batch_id = False
        return res

    def process_cancel_backorder(self):
        res = super().process_cancel_backorder()
        if self.env.context.get('pickings_to_detach'):
            self.env['stock.picking'].browse(self.env.context['pickings_to_detach']).batch_id = False
        return res
