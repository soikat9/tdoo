# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class Website(models.Model):
    _inherit = 'website'

    def sale_product_domain(self):
        return ['&'] + super(Website, self).sale_product_domain() + [('detailed_type', '!=', 'event_booth')]
