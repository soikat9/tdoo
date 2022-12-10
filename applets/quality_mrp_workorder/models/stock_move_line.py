# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    def _without_quality_checks(self):
        self.ensure_one()
        return super()._without_quality_checks() or not self.quality_check_ids.filtered(lambda qc: qc.measure_on != 'product')
