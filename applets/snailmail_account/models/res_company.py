# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class Company(models.Model):
    _inherit = "res.company"

    invoice_is_snailmail = fields.Boolean(string='Send by Post', default=False)
