# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import models


class Task(models.Model):
    _inherit = "project.task"

    def _is_fsm_report_available(self):
        return super()._is_fsm_report_available() or self.sale_order_id
