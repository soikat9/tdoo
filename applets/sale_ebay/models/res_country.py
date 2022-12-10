# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


class ResCountry(models.Model):
    _inherit = "res.country"

    ebay_available = fields.Boolean("Use on eBay", help="If activated, can be used for eBay.")
