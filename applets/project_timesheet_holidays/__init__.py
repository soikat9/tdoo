# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models


def post_init(cr, registry):
    """ Set the timesheet project and task on existing leave type. Do it in post_init to
        be sure the internal project/task of res.company are set. (Since timesheet_generate field
        is true by default, those 2 fields are required on the leave type).
    """
    from tele import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    for hr_leave_type in env['hr.leave.type'].search([('timesheet_generate', '=', True), ('timesheet_project_id', '=', False)]):
        company = hr_leave_type.company_id or env.company
        hr_leave_type.write({
            'timesheet_project_id': company.internal_project_id.id,
            'timesheet_task_id': company.leave_timesheet_task_id.id,
        })
