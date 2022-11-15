# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models


class SignRequestSendCopy(models.TransientModel):
    _name = 'sign.request.send.copy'
    _description = 'Sign send request copy'

    request_id = fields.Many2one(
        'sign.request',
        default=lambda self: self.env.context.get('active_id', None),
    )
    partner_ids = fields.Many2many('res.partner', string="Contact")

    def send_a_copy(self):
        return self.env['sign.request'].add_followers(self.request_id.id, self.partner_ids.ids)
