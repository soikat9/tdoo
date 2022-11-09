# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, _
from tele.exceptions import UserError


class SaleOrderMondialRelay(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        unmatch = self.filtered(lambda so: so.carrier_id.is_mondialrelay != so.partner_shipping_id.is_mondialrelay)
        if unmatch:
            error = _('Mondial Relay mismatching between delivery method and shipping address.')
            if len(self) > 1:
                error += ' (%s)' % ','.join(unmatch.mapped('name'))
            raise UserError(error)
        return super().action_confirm()
