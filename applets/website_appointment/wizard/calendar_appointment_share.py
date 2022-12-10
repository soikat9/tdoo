# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models
from tele.osv.expression import AND


class CalendarWebsiteAppointmentShare(models.TransientModel):
    _inherit = 'calendar.appointment.share'

    def _domain_appointment_type_ids(self):
        domain = super()._domain_appointment_type_ids()
        return AND([domain, [('is_published', '!=', False)]])
