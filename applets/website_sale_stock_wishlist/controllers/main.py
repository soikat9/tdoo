# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import http
from tele.http import request
from tele.applets.website_sale.controllers.main import WebsiteSale


class WebsiteSaleStockWishlist(WebsiteSale):
    @http.route(['/shop/wishlist/notify/<model("product.wishlist"):wish>'], type='json', auth="public", website=True)
    def notify_stock(self, wish, notify=True, **kw):
        if not request.website.is_public_user():
            wish['stock_notification'] = notify
        return wish['stock_notification']
