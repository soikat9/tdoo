# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class Forecast(models.Model):

    _inherit = 'planning.slot'

    order_line_id = fields.Many2one('sale.order.line', string='Sales Order Line', related="task_id.sale_line_id", store=True, readonly=False)
