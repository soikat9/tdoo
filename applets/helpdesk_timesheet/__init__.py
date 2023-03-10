# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models
from . import wizard
from . import report

from tele import api, SUPERUSER_ID


def _helpdesk_timesheet_post_init(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    teams = env['helpdesk.team'].search([('use_helpdesk_timesheet', '=', True), ('project_id', '=', False), ('use_helpdesk_sale_timesheet', '=', False)])

    for team in teams:
        team.project_id = team._create_project(team.name, team.use_helpdesk_sale_timesheet, {'allow_timesheets': True, 'allow_timesheets': True})
        env['helpdesk.ticket'].search([('team_id', '=', team.id), ('project_id', '=', False)]).write({'project_id': team.project_id.id})
