# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from datetime import timedelta

from tele.fields import Datetime
from tele.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestUi(HttpCase):

    def test_event_configurator(self):

        event = self.env['event.event'].create({
            'name': 'Design Fair Los Angeles',
            'date_begin': Datetime.now() + timedelta(days=1),
            'date_end': Datetime.now() + timedelta(days=5),
        })

        self.env['event.event.ticket'].create([{
            'name': 'Standard',
            'event_id': event.id,
            'product_id': self.env.ref('event_sale.product_product_event').id,
        }, {
            'name': 'VIP',
            'event_id': event.id,
            'product_id': self.env.ref('event_sale.product_product_event').id,
        }])
        self.start_tour("/web", 'event_configurator_tour', login="admin")