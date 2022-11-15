# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _planning_slot_values(self):
        return {
            **super()._planning_slot_values(),
            'project_id': self.project_id.id or self.task_id.project_id.id,
            'task_id': self.task_id.id,
        }
