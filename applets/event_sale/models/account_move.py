# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_invoice_paid(self):
        """ When an invoice linked to a sales order selling registrations is
        paid confirm attendees. Attendees should indeed not be confirmed before
        full payment. """
        res = super(AccountMove, self).action_invoice_paid()
        self.mapped('line_ids.sale_line_ids')._update_registrations(confirm=True, mark_as_paid=True)
        return res
