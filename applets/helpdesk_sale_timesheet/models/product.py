# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    sla_id = fields.Many2one(
        "helpdesk.sla", string="SLA Policy",
        company_dependent=True,
        domain="[('company_id', '=', current_company_id)]")
