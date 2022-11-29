# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class CouponReport(models.AbstractModel):
    _name = 'report.coupon.report_coupon'
    _description = 'Sales Coupon Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['coupon.coupon'].browse(docids)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'coupon.coupon',
            'data': data,
            'docs': docs,
        }
