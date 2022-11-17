# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models, _
from tele.exceptions import UserError


class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    hide_location = fields.Boolean(compute='_compute_hide_location')

    @api.depends('approval_type', 'has_location')
    def _compute_hide_location(self):
        multi_warehouse = self.user_has_groups('stock.group_stock_multi_warehouses')
        for request in self:
            request.hide_location = (
                request.has_location == 'no' or (multi_warehouse and request.approval_type == 'purchase')
            )