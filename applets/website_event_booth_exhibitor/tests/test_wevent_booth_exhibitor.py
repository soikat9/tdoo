# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.base.tests.common import HttpCaseWithUserDemo, HttpCaseWithUserPortal
from tele.tests import tagged


@tagged('post_install', '-at_install')
class TestWEventBoothExhibitorCommon(HttpCaseWithUserDemo, HttpCaseWithUserPortal):

    def test_register(self):
        self.browser_js(
            '/event',
            'tele.__DEBUG__.services["web_tour.tour"].run("webooth_exhibitor_register")',
            'tele.__DEBUG__.services["web_tour.tour"].tours.webooth_exhibitor_register.ready',
            login='admin'
        )
