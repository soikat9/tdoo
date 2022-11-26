# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, api, fields
from tele.tools.translate import _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    website_id = fields.Many2one('website', related='sale_id.website_id', string='Website',
                                 help='Website this picking belongs to.',
                                 store=True, readonly=True)

