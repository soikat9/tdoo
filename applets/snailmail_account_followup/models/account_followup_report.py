# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models, fields


class AccountFollowupReport(models.AbstractModel):
    _inherit = "account.followup.report"

    def _get_line_info(self, followup_line):
        res = super(AccountFollowupReport , self)._get_line_info(followup_line)
        res.update(send_letter=followup_line.send_letter)
        return res
