# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from .common import SpreadsheetTestCommon

from tele.tests import tagged
from tele.tests.common import HttpCase

@tagged("post_install", "-at_install")
class TestSpreadsheetOpenPivot(SpreadsheetTestCommon, HttpCase):

    def test_01_spreadsheet_open_pivot_as_admin(self):
        self.start_tour("/web", "spreadsheet_open_pivot_sheet", login="admin")

    def test_01_spreadsheet_open_pivot_as_user(self):
        self.start_tour("/web", "spreadsheet_open_pivot_sheet", login="spreadsheetDude")
