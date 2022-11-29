# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details

from tele import models, fields, api

class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    icon_img = fields.Image("Menu New Image")
    use_icon = fields.Boolean("Use Icon")
    icon_class_name = fields.Char("Icon Class Name")
