# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def action_new_quotation(self):
        action = super().action_new_quotation()
        # Make the lead's Assigned Partner the quotation's Referrer.
        action['context']['default_referrer_id'] = self.partner_assigned_id.id
        return action
