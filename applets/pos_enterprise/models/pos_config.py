# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    module_pos_iot = fields.Boolean('IoT Box', related="is_posbox")
