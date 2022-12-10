# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class ProjectProjectStage(models.Model):
    _name = 'project.project.stage'
    _description = 'Project Stage'
    _order = 'sequence, id'

    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=50)
    name = fields.Char(required=True, translate=True)
    mail_template_id = fields.Many2one('mail.template', string='Email Template', domain=[('model', '=', 'project.project')],
        help="If set, an email will be sent to the customer when the project reaches this step.")
    fold = fields.Boolean('Folded in Kanban', help="This stage is folded in the kanban view.")
