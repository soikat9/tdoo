# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models, _
from tele.exceptions import UserError


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    is_subcontract = fields.Boolean(store=False, search='_search_is_subcontract')

    def _search_is_subcontract(self, operator, value):
        if operator not in ['=', '!='] or not isinstance(value, bool):
            raise UserError(_('Operation not supported'))

        subcontract_locations = self.env['res.company'].search([]).subcontracting_location_id

        quant_ids = self.env['stock.quant'].search([
            ('location_id', 'in', subcontract_locations.ids),
        ]).ids
        if (operator == '!=' and value is True) or (operator == '=' and value is False):
            domain_operator = 'not in'
        else:
            domain_operator = 'in'
        return [('id', domain_operator, quant_ids)]
