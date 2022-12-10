# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    lead_mining_request_id = fields.Many2one('crm.iap.lead.mining.request', string='Lead Mining Request', index=True)
