# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.tests import tagged
from tele.applets.auth_totp.tests.test_totp import TestTOTP


@tagged('post_install', '-at_install')
class TestTOTPInvite(TestTOTP):

    def test_totp_administration(self):
        self.start_tour('/web', 'totp_admin_invite', login='admin')
        self.start_tour('/web', 'totp_admin_self_invite', login='admin')
