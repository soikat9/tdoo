# coding: utf-8
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_social_demo = fields.Boolean('Enable Demo Mode', groups="base.group_system")
