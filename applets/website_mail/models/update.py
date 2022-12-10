# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class PublisherWarrantyContract(models.AbstractModel):
    _inherit = "publisher_warranty.contract"

    @api.model
    def _get_message(self):
        msg = super(PublisherWarrantyContract, self)._get_message()
        msg['website'] = True
        return msg
