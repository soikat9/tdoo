# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    rental_sign_tmpl_id = fields.Many2one(
        "sign.template",
        related="company_id.rental_sign_tmpl_id",
        string="Default Document",
        help="Set a default document template for all rentals in the current company",
        readonly=False,
    )
