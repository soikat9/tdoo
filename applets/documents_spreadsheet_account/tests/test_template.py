# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from unittest.mock import patch

import tele
from tele.tests import tagged
from tele.tests.common import HttpCase


@tagged('post_install', '-at_install')
class TestSpreadsheetTemplate(HttpCase):

    def test_spreadsheet_template_montly_budget(self):
        self.start_tour('/web', 'spreadsheet_template_montly_budget', login='admin')

    def test_spreadsheet_template_quarterly_budget(self):
        self.start_tour('/web', 'spreadsheet_template_quarterly_budget', login='admin')

    def test_spreadsheet_template_sales_commission(self):
        self.start_tour('/web', 'spreadsheet_template_sales_commission', login='admin')
