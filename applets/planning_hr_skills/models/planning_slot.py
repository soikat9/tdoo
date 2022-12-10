# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class PlanningSlot(models.Model):
    _inherit = 'planning.slot'

    employee_skill_ids = fields.One2many(related='employee_id.employee_skill_ids', string='Skills')
