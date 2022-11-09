# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import random

from tele import models


class DemoSocialPost(models.Model):
    _inherit = 'social.post'

    def _compute_click_count(self):
        """ Let's add some random click statistics on our posts to make them look better. """
        for post in self:
            post.click_count = random.randint(10000, 30000)
