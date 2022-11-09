# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


# We add a field on this model
class Unit(models.Model):
    _inherit = 'test.unit'

    second_name = fields.Char()
