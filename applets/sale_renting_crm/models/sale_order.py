# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # same field as sale_crm, one will possibly override the other so their definition should stay in sync
    # sale_crm depends on sale_management and we don't want sale_renting_crm to install a new application
    # for a single button.
    # YTI TODO: sale_crm shoudn't depend on sale_management
    opportunity_id = fields.Many2one(
        "crm.lead", string="Opportunity", check_company=True,
        domain="[('type', '=', 'opportunity'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )
