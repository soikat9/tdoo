# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import tele.tests

@tele.tests.tagged("post_install", "-at_install")
class TestTeleEditor(tele.tests.HttpCase):

    def test_tele_editor_suite(self):
        self.browser_js('/web_editor/static/lib/tele-editor/test/editor-test.html', "", "", timeout=1800)
