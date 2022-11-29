# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
# Copyright (C) 2004-2008 PC Solutions (<http://pcsol.be>). All Rights Reserved
from tele import fields, models, api, _
from tele.exceptions import ValidationError

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    pos_payment_method_ids = fields.One2many('pos.payment.method', 'journal_id', string='Point of Sale Payment Methods')

    @api.constrains('type')
    def _check_type(self):
        methods = self.env['pos.payment.method'].sudo().search([("journal_id", "in", self.ids)])
        if methods:
            raise ValidationError(_("This journal is associated with a payment method. You cannot modify its type"))
