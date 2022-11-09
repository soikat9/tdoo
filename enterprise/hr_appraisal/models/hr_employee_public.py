# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models, tools


class HrEmployeePublic(models.Model):
    _inherit = "hr.employee.public"

    last_appraisal_id = fields.Many2one(readonly=True)
