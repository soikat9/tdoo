# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class ReportStockRule(models.AbstractModel):
    _inherit = 'report.stock.report_stock_rule'

    @api.model
    def _get_rule_loc(self, rule, product_id):
        """ We override this method to handle buy rules which do not have a location_src_id.
        """
        res = super(ReportStockRule, self)._get_rule_loc(rule, product_id)
        if rule.action == 'buy':
            res['source'] = self.env.ref('stock.stock_location_suppliers')
        return res
