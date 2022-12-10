  
# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class MrpProductionWorkcenterLine(models.Model):
    _inherit = "mrp.workorder"

    def action_worksheet_check(self):
        self.ensure_one()
        self.current_quality_check_id.action_worksheet_check()
        return self._next()

    def action_fill_sheet(self):
        self.ensure_one()
        return self.current_quality_check_id.action_quality_worksheet()
