# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class Users(models.Model):
    _inherit = 'res.users'

    target_sales_won = fields.Integer('Won in Opportunities Target')
    target_sales_done = fields.Integer('Activities Done Target')
