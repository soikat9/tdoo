# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    rental_sign_tmpl_id = fields.Many2one(
        "sign.template",
        string="Default Document Template for Rentals",
        help="This document template will be selected by default when signing "
        "documents from a rental order. You should select a template accessible "
        "to all Sign users.",
    )
