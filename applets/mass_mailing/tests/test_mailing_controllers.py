# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import werkzeug

from tele.applets.mass_mailing.tests.common import MassMailCommon
from tele.tests.common import HttpCase


class TestMassMailingControllers(MassMailCommon, HttpCase):

    def test_tracking_url_token(self):
        mail_mail = self.env['mail.mail'].create({})

        response = self.url_open(mail_mail._get_tracking_url())
        self.assertEqual(response.status_code, 200)

        base_url = mail_mail.get_base_url()
        url = werkzeug.urls.url_join(base_url, 'mail/track/%s/fake_token/blank.gif' % mail_mail.id)

        response = self.url_open(url)
        self.assertEqual(response.status_code, 400)
