# For full licensing and copyright information, see the LICENSE file - Tele, INC.
# -*- coding: utf-8 -*-

from tele.tests import HttpCase, tagged

@tagged('-at_install', 'post_install')
class TestRecordTime(HttpCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.env['project.project'].create({
            'name': 'Test Project'
        })

    def test_record_time(self):
        self.start_tour('/web', 'timesheet_record_time', login='admin', timeout=100)
