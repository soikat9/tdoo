# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class MrpDocument(models.Model):
    _inherit = 'mrp.document'

    origin_attachment_id = fields.Many2one('ir.attachment')
