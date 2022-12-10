# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class CalendarLeaves(models.Model):
    _inherit = "resource.calendar.leaves"

    holiday_id = fields.Many2one("hr.leave", string='Leave Request')
