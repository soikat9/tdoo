# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    quality_check_ids = fields.One2many('quality.check', 'move_line_id', string='Check')

    def _without_quality_checks(self):
        self.ensure_one()
        return not self.quality_check_ids
