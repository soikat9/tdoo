# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    margin = fields.Float('Margin')

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['margin'] = ", SUM(l.margin / CASE COALESCE(s.currency_rate, 0) WHEN 0 THEN 1.0 ELSE s.currency_rate END) AS margin"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
