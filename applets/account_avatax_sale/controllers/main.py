# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele.applets.sale.controllers.portal import CustomerPortal
from tele.applets.sale_management.controllers.portal import CustomerPortal as CustomerPortalSaleManagement

from tele import http


class CustomerPortalAvatax(CustomerPortal):
    @http.route([
        '/my/orders/<int:order_id>',
    ], type='http', auth='public', website=True)
    def portal_order_page(self, order_id=None, **post):
        response = super(CustomerPortalAvatax, self).portal_order_page(order_id=order_id, **post)
        if 'sale_order' not in response.qcontext:
            return response

        # Update taxes before customers see their quotation. This also ensures that tax validation
        # works (e.g. customer has valid address, ...). Otherwise errors will occur during quote
        # confirmation.
        order = response.qcontext['sale_order']
        if order.state in ('draft', 'sent') and order.fiscal_position_id.is_avatax:
            order.button_update_avatax()

        return response


class CustomerPortalSaleManagementAvatax(CustomerPortalSaleManagement):
    def _get_portal_order_details(self, order_sudo, order_line=False):
        if order_sudo.fiscal_position_id.is_avatax:
            order_sudo.button_update_avatax()

        return super()._get_portal_order_details(order_sudo, order_line=order_line)
