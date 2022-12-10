# For full licensing and copyright information, see the LICENSE file - Tele, INC.
# -*- coding: utf-8 -*-

import tele.tests


@tele.tests.tagged('post_install', '-at_install')
class TestUi(tele.tests.HttpCase):
    def test_ui(self):
        self.start_tour("/web", 'helpdesk_tour', login="admin")
