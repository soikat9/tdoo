# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class ResCountry(models.Model):
    _inherit = 'res.country'

    def get_website_sale_countries(self, mode='billing'):
        return self.sudo().search([])

    def get_website_sale_states(self, mode='billing'):
        return self.sudo().state_ids
