# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class QualityPoint(models.Model):
    _inherit = "quality.point"

    device_id = fields.Many2one('iot.device', ondelete='restrict', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
