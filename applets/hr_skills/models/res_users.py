# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import fields, models


class User(models.Model):
    _inherit = ['res.users']

    resume_line_ids = fields.One2many(related='employee_id.resume_line_ids', readonly=False)
    employee_skill_ids = fields.One2many(related='employee_id.employee_skill_ids', readonly=False)

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ['resume_line_ids', 'employee_skill_ids']

    @property
    def SELF_WRITEABLE_FIELDS(self):
        return super().SELF_WRITEABLE_FIELDS + ['resume_line_ids', 'employee_skill_ids']
