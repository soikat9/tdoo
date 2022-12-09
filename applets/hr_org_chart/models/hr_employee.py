# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class Employee(models.Model):
    _inherit = ["hr.employee"]

    subordinate_ids = fields.One2many('hr.employee', string='Subordinates', compute='_compute_subordinates', help="Direct and indirect subordinates",
                                      compute_sudo=True)


class HrEmployeePublic(models.Model):
    _inherit = ["hr.employee.public"]

    subordinate_ids = fields.One2many('hr.employee.public', string='Subordinates', compute='_compute_subordinates', help="Direct and indirect subordinates",
                                      compute_sudo=True)
