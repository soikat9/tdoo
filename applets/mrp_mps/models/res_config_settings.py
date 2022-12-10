# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    manufacturing_period = fields.Selection(related="company_id.manufacturing_period", string="Manufacturing Period", readonly=False)
    manufacturing_period_to_display = fields.Integer(
        related='company_id.manufacturing_period_to_display',
        string='Number of Manufacturing Period Columns', readonly=False)
