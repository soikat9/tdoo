# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _is_add_to_cart_allowed(self):
        # `event_booth_registration_confirm` calls `_cart_update` with specific products, allow those aswell.
        return super()._is_add_to_cart_allowed() or\
                self.env['event.booth.category'].sudo().search_count([('product_id', '=', self.id)])
