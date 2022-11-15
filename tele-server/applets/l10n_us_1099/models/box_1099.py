# coding: utf-8
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import models, fields


class Box1099(models.Model):
    _name = "l10n_us.1099_box"
    _description = "Represents a box on a 1099 box."

    name = fields.Char("Name")
