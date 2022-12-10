# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import tele.tests


@tele.tests.tagged('post_install', '-at_install')
class TestUi(tele.tests.HttpCase):

    def test_01_project_tour(self):
        self.start_tour("/web", 'project_tour', login="admin")
