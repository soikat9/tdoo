# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class PublishedFoo(models.Model):
    _name = 'test_new_api.foo'
    _inherit = ['test_new_api.foo', 'test_inherit.mixin']
