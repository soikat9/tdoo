# -*- coding:utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


class HrPayrollStructureType(models.Model):
    _inherit = 'hr.payroll.structure.type'
    _description = 'Salary Structure Type'

    salary_advantage_ids = fields.One2many('hr.contract.salary.advantage', 'structure_type_id')