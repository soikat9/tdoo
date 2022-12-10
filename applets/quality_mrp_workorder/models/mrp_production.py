# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    check_ids = fields.One2many('quality.check', domain=[('workorder_id', '=', False)])
