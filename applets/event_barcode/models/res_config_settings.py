# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    barcode_nomenclature_id = fields.Many2one('barcode.nomenclature', related='company_id.nomenclature_id', readonly=False)
