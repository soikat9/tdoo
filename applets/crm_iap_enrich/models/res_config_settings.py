# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    @api.model
    def get_values(self):
        values = super(ResConfigSettings, self).get_values()
        cron = self.sudo().with_context(active_test=False).env.ref('crm_iap_enrich.ir_cron_lead_enrichment', raise_if_not_found=False)
        values['lead_enrich_auto'] = 'auto' if cron and cron.active else 'manual'
        return values

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        cron = self.sudo().with_context(active_test=False).env.ref('crm_iap_enrich.ir_cron_lead_enrichment', raise_if_not_found=False)
        if cron:
            cron.active = self.lead_enrich_auto == 'auto'
