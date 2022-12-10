# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResCountry(models.Model):
    _inherit = 'res.country'

    intrastat = fields.Boolean(string='Intrastat member')
