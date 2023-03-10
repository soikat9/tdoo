# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.tests import tagged
from tele.tests.common import HttpCase


@tagged("post_install", "-at_install")
class TestSpreadsheetCreateEmpty(HttpCase):
    def test_01_spreadsheet_create_empty(self):
        self.start_tour("/web", "spreadsheet_create_empty_sheet", login="admin")

    def test_02_spreadsheet_create_list_view(self):
        self.start_tour("/web", "spreadsheet_create_list_view", login="admin")
