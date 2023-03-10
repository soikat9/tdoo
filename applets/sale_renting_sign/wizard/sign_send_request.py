# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import fields, models


class SignSendRequest(models.TransientModel):
    _inherit = "sign.send.request"

    sale_order_id = fields.Many2one("sale.order", string="Sales Order")

    def create_request(self, send=True, without_mail=False):
        request_info = super(SignSendRequest, self).create_request(send, without_mail)
        request_id = request_info["id"]
        if self.sale_order_id:
            request = self.env["sign.request"].browse(request_id)
            request.sale_order_id = self.sale_order_id
        return request_info
