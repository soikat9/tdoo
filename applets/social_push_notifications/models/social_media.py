# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


class SocialMediaPushNotifications(models.Model):
    _inherit = 'social.media'

    media_type = fields.Selection(selection_add=[('push_notifications', 'Push Notifications')])

    def _action_add_account(self):
        self.ensure_one()

        if self.media_type != 'push_notifications':
            return super(SocialMediaPushNotifications, self)._action_add_account()

        return None
