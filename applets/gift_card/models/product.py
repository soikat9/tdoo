# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import _, api, fields, models
from tele.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    detailed_type = fields.Selection(selection_add=[
        ('gift', 'Gift Card'),
    ], ondelete={'gift': 'set service'})

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['gift'] = 'service'
        return type_mapping

    @api.ondelete(at_uninstall=False)
    def _unlink_gift_card_product(self):
        if self.env.ref('gift_card.pay_with_gift_card_product').product_tmpl_id in self:
            raise UserError(_('Deleting the Gift Card Pay product is not allowed.'))
