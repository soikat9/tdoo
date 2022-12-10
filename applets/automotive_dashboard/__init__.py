# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele.api import Environment, SUPERUSER_ID

def uninstall_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    env.ref('automotive.automotive_costs_reporting_action').write({'view_mode': 'graph,pivot'})