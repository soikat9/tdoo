# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class Page(models.Model):
    _inherit = 'website.page'

    @classmethod
    def _get_cached_blacklist(cls):
        return super()._get_cached_blacklist() + (
            # Contains a form with a dynamically added CSRF token
            'data-snippet="s_donation"',
        )
