# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    google_gmail_client_identifier = fields.Char('Gmail Client Id', config_parameter='google_gmail_client_id')
    google_gmail_client_secret = fields.Char('Gmail Client Secret', config_parameter='google_gmail_client_secret')
