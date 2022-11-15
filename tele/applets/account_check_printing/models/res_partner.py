# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


from tele import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    property_payment_method_id = fields.Many2one(
        comodel_name='account.payment.method',
        string='Payment Method',
        company_dependent=True,
        domain="[('payment_type', '=', 'outbound')]",
        help="Preferred payment method when paying this vendor. This is used to filter vendor bills"
             " by preferred payment method to register payments in mass. Use cases: create bank"
             " files for batch wires, check runs.",
    )
