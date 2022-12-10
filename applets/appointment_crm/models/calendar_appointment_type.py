# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class CalendarAppointmentType(models.Model):
    _inherit = "calendar.appointment.type"

    lead_create = fields.Boolean(string="Create Opportunities",
        help="For each scheduled appointment, create a new opportunity and assign it to the responsible employee.")
