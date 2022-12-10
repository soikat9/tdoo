# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class HrEmployeePublic(models.Model):
    _inherit = "hr.employee.public"

    first_contract_date = fields.Date(related='employee_id.first_contract_date', groups="base.group_user")
