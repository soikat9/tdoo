# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    planning_generation_interval = fields.Integer("Rate Of Shift Generation", required=True, readonly=False, default=6, help="Delay for the rate at which recurring shift should be generated in month")

    planning_allow_self_unassign = fields.Boolean("Can Employee Un-Assign Themselves?", default=False,
        help="Let your employees un-assign themselves from shifts when unavailable")

    planning_self_unassign_days_before = fields.Integer("Days before shift for unassignment", help="Deadline in days for shift unassignment")

    _sql_constraints = [('planning_self_unassign_days_before_positive', 'CHECK(planning_self_unassign_days_before >= 0)', "The amount of days before unassignment must be positive or equal to zero.")]
