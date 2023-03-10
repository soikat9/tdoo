# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.tests import HttpCase


class TestBusController(HttpCase):
    def test_health(self):
        response = self.url_open('/longpolling/health')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['status'], 'pass')
        self.assertNotIn('session_id', response.cookies)
