# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    warehouse_id = fields.Many2one('stock.warehouse', 'Warehouse', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['warehouse_id'] = ", s.warehouse_id as warehouse_id"
        groupby += ', s.warehouse_id'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
