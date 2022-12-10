# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, _


class MarketingTrace(models.Model):
    _inherit = 'marketing.trace'

    def process_event(self, action):
        self.ensure_one()
        super_result = super(MarketingTrace, self).process_event(action)
        if super_result:
            opened_child = self.child_ids.filtered(lambda trace: trace.state == 'scheduled')
            if action == 'sms_click':
                opened_child.filtered(
                    lambda trace: trace.activity_id.trigger_type == 'sms_not_click'
                ).action_cancel(message=_('Parent activity SMS clicked'))

            elif action == 'sms_bounce':
                opened_child.filtered(
                    lambda trace: trace.activity_id.trigger_type != 'sms_bounce'
                ).action_cancel(message=_('Parent activity SMS bounced'))

        return super_result
