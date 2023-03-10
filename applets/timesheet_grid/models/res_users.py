# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models


class User(models.Model):
    _inherit = ['res.users']

    timesheet_manager_id = fields.Many2one(related='employee_id.timesheet_manager_id')

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ['timesheet_manager_id']
