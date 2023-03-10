# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models, _
from tele.exceptions import UserError


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    holiday_id = fields.Many2one("hr.leave", string='Leave Request', copy=False)
    global_leave_id = fields.Many2one("resource.calendar.leaves", string="Global Time Off", ondelete='cascade')

    @api.ondelete(at_uninstall=False)
    def _unlink_except_linked_leave(self):
        if any(line.holiday_id for line in self):
            raise UserError(_('You cannot delete timesheets linked to time off. Please, cancel the time off instead.'))
