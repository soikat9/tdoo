# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import werkzeug

from tele import http
from tele.http import request
from tele.applets.website_event.controllers.main import WebsiteEventController


class WebsiteEventBoothController(WebsiteEventController):

    @http.route()
    def event_booth_main(self, event):
        pricelist = request.website.get_current_pricelist()
        if pricelist:
            event = event.with_context(pricelist=pricelist.id)
        return super(WebsiteEventBoothController, self).event_booth_main(event)

    @http.route()
    def event_booth_registration_confirm(self, event, booth_category_id, event_booth_ids, **kwargs):
        booths = self._get_requested_booths(event, event_booth_ids)
        booth_category = request.env['event.booth.category'].sudo().browse(int(booth_category_id))
        order = request.website.sale_get_order(force_create=1)
        order._cart_update(
            product_id=booth_category.product_id.id,
            set_qty=1,
            event_booth_pending_ids=booths.ids,
            registration_values=self._prepare_booth_registration_values(event, kwargs),
        )
        if order.amount_total:
            return request.redirect('/shop/checkout')
        elif order:
            order.action_confirm()
            request.website.sale_reset()

        return request.redirect(('/event/%s/booth/success?' % event.id) + werkzeug.urls.url_encode({
            'booths': ','.join([str(id) for id in booths.ids]),
        }))
