# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.base.tests.common import HttpCaseWithUserPortal
from tele.tests import tagged


@tagged('post_install', '-at_install')
class TestUi(HttpCaseWithUserPortal):
    def test_01_portal_load_tour(self):
        self.start_tour("/", 'portal_load_homepage', login="portal")
