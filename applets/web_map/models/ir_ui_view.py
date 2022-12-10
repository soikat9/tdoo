# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class View(models.Model):
    _inherit = 'ir.ui.view'

    type = fields.Selection(selection_add=[('map', "Map")])
