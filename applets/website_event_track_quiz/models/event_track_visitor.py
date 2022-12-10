# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class TrackVisitor(models.Model):
    _name = 'event.track.visitor'
    _inherit = ['event.track.visitor']

    quiz_completed = fields.Boolean('Completed')
    quiz_points = fields.Integer("Quiz Points", default=0)
