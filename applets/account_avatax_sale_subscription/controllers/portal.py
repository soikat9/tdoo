# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import http
from tele.applets.sale_subscription.controllers.portal import SaleSubscription, PaymentPortal

class SaleSubscriptionAvatax(SaleSubscription):
    @http.route()
    def subscription(self, subscription_id, access_token='', message='', message_class='', **kw):
        response = super().subscription(subscription_id, access_token=access_token, message=message, message_class=message_class, **kw)

        if 'account' not in response.qcontext:
            return response

        sub = response.qcontext['account']
        if sub.is_avatax:
            sub.button_update_avatax()

        return response


class PaymentPortalAvatax(PaymentPortal):
    def _create_invoice(self, subscription):
        res = super()._create_invoice(subscription)
        res.button_update_avatax()
        return res

