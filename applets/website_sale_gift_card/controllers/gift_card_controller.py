# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import http
from tele.http import request
from tele.applets.website_sale.controllers import main


class GiftCardController(main.WebsiteSale):

    @http.route('/shop/pay_with_gift_card', type='http', methods=['POST'], website=True, auth='public')
    def add_gift_card(self, gift_card_code, **post):
        gift_card = request.env["gift.card"].sudo().search([('code', '=', gift_card_code.strip())], limit=1)
        order = request.env['website'].get_current_website().sale_get_order()
        gift_card_status = order._pay_with_gift_card(gift_card)
        return request.redirect('/shop/payment' + '?keep_carrier=1' + ('&gift_card_error=%s' % gift_card_status if gift_card_status else ''))

    @http.route()
    def shop_payment(self, **post):
        order = request.website.sale_get_order()
        res = super().shop_payment(**post)
        order._recompute_gift_card_lines()
        return res

    @http.route(['/shop/cart'], type='http', auth="public", website=True)
    def cart(self, **post):
        order = request.website.sale_get_order()
        order._recompute_gift_card_lines()
        return super().cart(**post)

    def _get_shop_payment_values(self, order, **kwargs):
        values = super()._get_shop_payment_values(order, **kwargs)
        values['allow_pay_with_gift_card'] = True
        return values
