# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    quality_check_qty = fields.Integer(
        compute='_compute_quality_check_qty', groups='quality.group_quality_user')

    def _compute_quality_check_qty(self):
        for prod_lot in self:
            prod_lot.quality_check_qty = self.env['quality.check'].search_count([
                ('lot_id', '=', prod_lot.id),
                ('company_id', '=', self.env.company.id)
            ])
