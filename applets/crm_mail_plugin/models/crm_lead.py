# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def _form_view_auto_fill(self):
        """
            deprecated as of saas-14.3, not needed for newer versions of the mail plugin but necessary
            for supporting older versions
        """
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'crm.lead',
            'context': {
                'default_partner_id': self.env.context.get('params', {}).get('partner_id'),
            }
        }
