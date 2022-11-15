# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class QualityCheck(models.Model):
    _inherit = "quality.check"

    ip = fields.Char(related='point_id.device_id.iot_id.ip')
    identifier = fields.Char(related='point_id.device_id.identifier')
    device_name = fields.Char(related='point_id.device_id.name', size=30, string='Device Name: ')
