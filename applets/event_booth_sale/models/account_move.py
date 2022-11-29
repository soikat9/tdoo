# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_invoice_paid(self):
        """ When an invoice linked to a sales order selling registrations is
        paid, update booths accordingly as they are booked when invoice is paid.
        """
        res = super(AccountMove, self).action_invoice_paid()
        self.mapped('line_ids.sale_line_ids')._update_event_booths(set_paid=True)
        return res
