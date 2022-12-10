# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    hs_code = fields.Char(
        string="HS Code",
        help="Standardized code for international shipping and goods declaration. At the moment, only used for the FedEx shipping provider.",
    )
