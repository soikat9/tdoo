# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
import tele.tests
from tele.osv import expression


@tele.tests.tagged('post_install', '-at_install', 'assets_bundle')
class BusWebTests(tele.tests.HttpCase):

    def test_bundle_sends_bus(self):
        """
        Tests two things:
        - Messages are posted to the bus when assets change
          i.e. their hash has been recomputed and differ from the attachment's
        - The interface deals with those bus messages by displaying one notification
        """
        db_name = self.env.registry.db_name
        bundle_xml_ids = ('web.assets_common', 'web.assets_backend')

        domain = []
        for bundle in bundle_xml_ids:
            domain = expression.OR([
                domain,
                [('name', 'ilike', bundle + '%')]
            ])
        # start from a clean slate
        self.env['ir.attachment'].search(domain).unlink()
        self.env.registry._clear_cache()

        sendones = []
        def patched_sendone(self, channel, notificationType, message):
            """ Control API and number of messages posted to the bus linked to
            bundle_changed events """
            if notificationType == 'bundle_changed':
                sendones.append((channel, message))

        self.patch(type(self.env['bus.bus']), '_sendone', patched_sendone)

        self.authenticate('admin', 'admin')
        self.url_open('/web')

        # One sendone for each asset bundle and for each CSS / JS
        self.assertEqual(
            len(sendones),
            4,
            'Received %s' % '\n'.join('%s - %s' % (tmp[0], tmp[1]) for tmp in sendones)
        )
        for (channel, message) in sendones:
            self.assertEqual(channel, 'broadcast')
            self.assertEqual(len(message), 1)
            self.assertTrue(isinstance(message.get('server_version'), str))
