# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class MassMailing(models.Model):
    _inherit = 'mailing.mailing'

    def _send_sms_get_composer_values(self, res_ids):
        composer_values = super(MassMailing, self)._send_sms_get_composer_values(res_ids)
        if self.env.context.get('default_marketing_activity_id'):
            composer_values['marketing_activity_id'] = self.env.context['default_marketing_activity_id']
        return composer_values
