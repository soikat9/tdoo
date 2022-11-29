# -*- encoding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models


class QualityCheck(models.Model):
    _inherit = "quality.check"

    batch_id = fields.Many2one(related='picking_id.batch_id')
