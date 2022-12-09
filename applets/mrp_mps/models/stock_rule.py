# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _make_po_get_domain(self, company_id, values, partner):
        """ Avoid to merge two RFQ for the same MPS replenish. """
        domain = super(StockRule, self)._make_po_get_domain(company_id, values, partner)
        if self.env.context.get('skip_lead_time') and values.get('date_planned'):
            domain += (('date_planned_mps', '=', values['date_planned']),)
        return domain
