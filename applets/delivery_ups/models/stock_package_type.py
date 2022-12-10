# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import fields, models


class PackageType(models.Model):
    _inherit = 'stock.package.type'

    package_carrier_type = fields.Selection(selection_add=[('ups', 'UPS')])
