# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cal_microsoft_client_id = fields.Char("Microsoft Client_id", config_parameter='microsoft_calendar_client_id', default='')
    cal_microsoft_client_secret = fields.Char("Microsoft Client_key", config_parameter='microsoft_calendar_client_secret', default='')
