# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    timesheet_cost = fields.Monetary('Timesheet Cost', currency_field='currency_id',
    	groups="hr.group_hr_user", default=0.0)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', readonly=True)
