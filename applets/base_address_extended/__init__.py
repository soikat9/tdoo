# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models
from tele import api, SUPERUSER_ID


def _update_street_format(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    specific_countries = env['res.country'].search([('street_format', '!=', '%(street_number)s/%(street_number2)s %(street_name)s')])
    env['res.partner'].search([('country_id', 'in', specific_countries.ids)])._compute_street_data()
