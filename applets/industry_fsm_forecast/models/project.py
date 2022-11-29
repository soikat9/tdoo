# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models


class Project(models.Model):
    _inherit = 'project.project'

    allow_forecast = fields.Boolean(compute='_compute_allow_forecast', store=True, readonly=False)

    @api.depends('is_fsm')
    def _compute_allow_forecast(self):
        for project in self:
            if not project._origin:
                project.allow_forecast = not project.is_fsm
