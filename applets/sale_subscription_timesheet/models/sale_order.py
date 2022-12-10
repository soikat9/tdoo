# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _action_confirm(self):
        res = super(SaleOrder, self)._action_confirm()
        for so in self:
            if so.analytic_account_id:
                for sub in so.order_line.mapped('subscription_id'):
                    sub.sudo().analytic_account_id = so.analytic_account_id
        return res


