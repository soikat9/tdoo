# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from collections import defaultdict

from tele import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _action_confirm(self, merge=True, merge_into=False):
        moves = super(StockMove, self)._action_confirm(merge=merge, merge_into=merge_into)

        # Groupby move by production order. Use it in order to generate missing quality checks.
        mo_moves = defaultdict(lambda: self.env['stock.move'])
        check_vals_list = []
        for move in moves:
            if move.production_id and not move.scrapped:
                mo_moves[move.production_id] |= move
        for production, moves in mo_moves.items():
            quality_points_domain = self.env['quality.point']._get_domain(moves.product_id, production.picking_type_id, measure_on='operation')
            quality_points_domain = self.env['quality.point']._get_domain_for_production(quality_points_domain)
            quality_points = self.env['quality.point'].sudo().search(quality_points_domain)

            # Since move lines are created too late for the manufactured product, we create the QC of lot type directly here instead, excluding by-products
            domain_lot_type = self.env['quality.point']._get_domain(production.product_id, production.picking_type_id, measure_on='product')
            quality_points_lot_type = self.env['quality.point'].sudo().search(domain_lot_type)

            quality_points = quality_points | quality_points_lot_type
            if not quality_points:
                continue
            mo_check_vals_list = quality_points._get_checks_values(moves.product_id, production.company_id.id, existing_checks=production.sudo().check_ids)
            for check_value in mo_check_vals_list:
                check_value.update({
                    'production_id': production.id,
                })
            check_vals_list += mo_check_vals_list
        self.env['quality.check'].sudo().create(check_vals_list)

        return moves
