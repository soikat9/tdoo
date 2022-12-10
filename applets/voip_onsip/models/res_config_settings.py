# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    wsServer = fields.Char(default='wss://edge.sip.onsip.com', config_parameter='voip.wsServer')
