# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models
from . import controllers

from tele import api, SUPERUSER_ID


def _website_helpdesk_slides_post_init(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    teams = env['helpdesk.team'].search([('use_website_helpdesk_slides', '=', True), ('elearning_id', '=', False)])
    elearnings_by_name = teams._create_elearnings_batch([{'name': team.name} for team in teams])
    for team in teams:
        team.elearning_id = elearnings_by_name.get(team.name)
