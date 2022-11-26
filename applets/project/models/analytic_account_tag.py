# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class AccountAnalyticTag(models.Model):
    _inherit = 'account.analytic.tag'

    task_ids = fields.Many2many('project.task', string='Tasks')
