#  -*- coding: utf-8 -*-
#  For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _get_fields_stock_barcode(self):
        """ Inject the field 'display_action_record_components' in the initial
        state of the barcode view.
        """
        fields = super()._get_fields_stock_barcode()
        fields.append('display_action_record_components')
        return fields
