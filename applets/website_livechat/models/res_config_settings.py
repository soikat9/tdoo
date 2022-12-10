# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    channel_id = fields.Many2one('im_livechat.channel', string='Website Live Channel', related='website_id.channel_id', readonly=False)
