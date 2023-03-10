# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.sms.tests import common as sms_common
from tele.applets.test_mail.tests.test_performance import BaseMailPerformance
from tele.tests.common import users, warmup
from tele.tests import tagged
from tele.tools import mute_logger


@tagged('mail_performance', 'post_install', '-at_install')
class TestSMSPerformance(BaseMailPerformance, sms_common.SMSCase):

    def setUp(self):
        super(TestSMSPerformance, self).setUp()
        self.user_employee.write({
            'login': 'employee',
            'country_id': self.env.ref('base.be').id,
        })
        self.admin = self.env.user

        self.customer = self.env['res.partner'].with_context(self._quick_create_ctx).create({
            'name': 'Test Customer',
            'email': 'test@example.com',
            'mobile': '0456123456',
            'country_id': self.env.ref('base.be').id,
        })
        self.test_record = self.env['mail.test.sms'].with_context(self._quick_create_ctx).create({
            'name': 'Test',
            'customer_id': self.customer.id,
            'phone_nbr': '0456999999',
        })

        # prepare recipients to test for more realistic workload
        Partners = self.env['res.partner'].with_context(self._quick_create_ctx)
        self.partners = self.env['res.partner']
        for x in range(0, 10):
            self.partners |= Partners.create({
                'name': 'Test %s' % x,
                'email': 'test%s@example.com' % x,
                'mobile': '0456%s%s0000' % (x, x),
                'country_id': self.env.ref('base.be').id,
            })

        self._init_mail_gateway()

    @mute_logger('tele.applets.sms.models.sms_sms')
    @users('employee')
    @warmup
    def test_message_sms_record_1_partner(self):
        record = self.test_record.with_user(self.env.user)
        pids = self.customer.ids
        with self.mockSMSGateway(), self.assertQueryCount(employee=21):
            messages = record._message_sms(
                body='Performance Test',
                partner_ids=pids,
            )

        self.assertEqual(record.message_ids[0].body, '<p>Performance Test</p>')
        self.assertSMSNotification([{'partner': self.customer}], 'Performance Test', messages)
