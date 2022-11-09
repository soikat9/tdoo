# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, SUPERUSER_ID

from . import models


def _populate_skills_for_confirmed(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    confirmed_appraisals = env['hr.appraisal'].search([('state', '=', 'pending'), ('skill_ids', '=', False)])
    confirmed_appraisals._copy_skills_when_confirmed()
