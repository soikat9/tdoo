# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, api


class Location(models.Model):
    _inherit = 'stock.location'
    _barcode_field = 'barcode'

    @api.model
    def _get_fields_stock_barcode(self):
        return ['display_name', 'barcode', 'parent_path']
