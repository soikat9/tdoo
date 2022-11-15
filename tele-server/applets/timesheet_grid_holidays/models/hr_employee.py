# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class Employee(models.Model):
    _inherit = 'hr.employee'

    def _get_timesheets_and_working_hours_query(self):
        return """
            SELECT aal.employee_id as employee_id, COALESCE(SUM(aal.unit_amount), 0) as worked_hours
            FROM account_analytic_line aal
            WHERE aal.employee_id IN %s AND date >= %s AND date <= %s AND aal.holiday_id is NULL AND aal.global_leave_id is NULL
            GROUP BY aal.employee_id
        """
