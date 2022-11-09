# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.tests import HttpCase, tagged

@tagged('-at_install', 'post_install')
class TestUi(HttpCase):
    def test_01_ui(self):
        self.start_tour("/", 'planning_test_tour', login='admin')
