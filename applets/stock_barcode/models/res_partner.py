# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _get_fields_stock_barcode(self):
        return ['display_name']
