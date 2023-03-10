# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from .taxcloud_request import TaxCloudRequest
from tele import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _get_TaxCloudRequest(self, api_id, api_key):
        return TaxCloudRequest(api_id, api_key)

    def _get_reward_values_free_shipping(self, program):
        res = super(SaleOrder, self)._get_reward_values_free_shipping(program)
        res.update(coupon_program_id=program.id)
        return res
