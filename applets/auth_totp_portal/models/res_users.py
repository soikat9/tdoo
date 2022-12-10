# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class Users(models.Model):
    _inherit = 'res.users'

    def get_totp_invite_url(self):
        if not self.has_group('base.group_user'):
            return '/my/security'
        else:
            return super(Users, self).get_totp_invite_url()
