import tele.tests
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


@tele.tests.tagged('post_install', '-at_install')
class TestUi(tele.tests.HttpCase):

    def test_01_sale_tour(self):
        self.start_tour("/web", 'sale_tour', login="admin", step_delay=100)
