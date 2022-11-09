# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pad_server = fields.Char(config_parameter='pad.pad_server', string="Pad Server")
    pad_key = fields.Char(config_parameter='pad.pad_key', string="Pad API Key")
