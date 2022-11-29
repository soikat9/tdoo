# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields, api, _


class User(models.Model):
    _inherit = ['res.users']

    vehicle = fields.Char(related="employee_id.vehicle")
    bank_account_id = fields.Many2one(related="employee_id.bank_account_id")

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ['vehicle', 'bank_account_id']
