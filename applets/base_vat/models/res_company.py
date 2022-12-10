# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    vat_check_vies = fields.Boolean(string='Verify VAT Numbers')
