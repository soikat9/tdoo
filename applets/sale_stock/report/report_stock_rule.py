# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class ReportStockRule(models.AbstractModel):
    _inherit = 'report.stock.report_stock_rule'

    @api.model
    def _get_routes(self, data):
        res = super(ReportStockRule, self)._get_routes(data)
        if data.get('so_route_ids'):
            res = self.env['stock.location.route'].browse(data['so_route_ids']) | res
        return res
