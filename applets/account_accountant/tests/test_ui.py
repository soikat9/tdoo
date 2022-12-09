# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import tele.tests


@tele.tests.tagged('-at_install', 'post_install')
class TestUi(tele.tests.HttpCase):
    def test_accountant_tour(self):
        self.start_tour("/web", 'account_accountant_tour', login="admin")
