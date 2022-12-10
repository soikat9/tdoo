# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class Company(models.Model):
    _inherit = "res.company"

    snailmail_color = fields.Boolean(string='Color', default=True)
    snailmail_cover = fields.Boolean(string='Add a Cover Page', default=False)
    snailmail_duplex = fields.Boolean(string='Both sides', default=False)
