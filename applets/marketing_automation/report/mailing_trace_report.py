# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models, tools


class MailingTraceReport(models.Model):
    _inherit = 'mailing.trace.report'

    def _report_get_request_where_items(self):
        res = super(MailingTraceReport, self)._report_get_request_where_items()
        res.append("mailing.use_in_marketing_automation IS NOT TRUE")
        return res
