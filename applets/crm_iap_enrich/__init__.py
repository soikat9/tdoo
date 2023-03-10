# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models

from tele.api import Environment, SUPERUSER_ID


def _synchronize_cron(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {'active_test': False})
    cron = env.ref('crm_iap_enrich.ir_cron_lead_enrichment')
    if cron:
        config = env['ir.config_parameter'].get_param('crm.iap.lead.enrich.setting', 'manual')
        cron.active = config != 'manual'
