# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, api

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.model
    def _grid_start_of(self, span, step, anchor):
        if span != 'year':
            return super(AccountAnalyticLine, self)._grid_start_of(span, step, anchor)
        return self.env.company.compute_fiscalyear_dates(anchor)['date_from']

    @api.model
    def _grid_end_of(self, span, step, anchor):
        if span != 'year':
            return super(AccountAnalyticLine, self)._grid_end_of(span, step, anchor)
        return self.env.company.compute_fiscalyear_dates(anchor)['date_to']
