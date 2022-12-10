# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.tests import common, tagged


@tagged('-at_install', 'post_install')
class TestAuthSignupUninvited(common.TransactionCase):

    def test_01_auth_signup_uninvited(self):
        self.env['website'].browse(1).auth_signup_uninvited = 'b2c'
        config = self.env['res.config.settings'].create({})
        self.assertEqual(config.auth_signup_uninvited, 'b2c')
