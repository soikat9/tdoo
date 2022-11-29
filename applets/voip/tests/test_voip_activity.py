# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from dateutil.relativedelta import relativedelta

from tele import fields
from tele.tests import common, tagged


@tagged('voip')
class TestVoipMailActivity(common.TransactionCase):

    def test_voip_activity_deadline(self):
        partner = self.env['res.partner'].create({
            'name': 'Freddy Krueger',
            'phone': '1234',
        })
        baseDate = fields.Date.today(self)
        activity = self.env['mail.activity'].create({
            'activity_type_id': self.env.ref('mail.mail_activity_data_call').id,
            'user_id': self.env.user.id,
            'date_deadline': baseDate,
            'res_id': partner.id,
            'res_model_id': self.env['ir.model']._get('res.partner').id,
        })
        phonecall = activity.voip_phonecall_id
        self.assertEqual(phonecall.date_deadline, baseDate, "Phonecall deadline should have been set")
        newdate = fields.Date.today(self) + relativedelta(days=2)
        activity.date_deadline = newdate
        self.assertEqual(phonecall.date_deadline, newdate, "Phonecall deadline should have been updated")
