# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    transfer_model_id = fields.Many2one('account.transfer.model', string="Originating Model")
