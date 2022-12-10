# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import models
from tele.http import request


class WabsitePage(models.AbstractModel):
    _inherit = 'website.page'

    def _get_cache_key(self, req):
        cart = request.website.sale_get_order()
        cache_key = (cart and cart.cart_quantity or 0,)
        cache_key += super()._get_cache_key(req)
        return cache_key
