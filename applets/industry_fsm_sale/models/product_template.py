# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    project_id = fields.Many2one(domain="[('company_id', '=', current_company_id), ('allow_billable', '=', True), '|', ('pricing_type', '=', 'task_rate'), ('is_fsm', '=', True), ('allow_timesheets', 'in', [service_policy == 'delivered_timesheet', True])]")
