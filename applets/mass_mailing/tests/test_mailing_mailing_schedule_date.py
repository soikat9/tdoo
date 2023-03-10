# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from datetime import datetime

from tele.applets.mass_mailing.tests.common import MassMailCommon
from tele.tests import users, Form
from tele.tools import mute_logger


class TestMailingScheduleDateWizard(MassMailCommon):

    @mute_logger('tele.applets.mail.models.mail_mail')
    @users('user_marketing')
    def test_mailing_schedule_date(self):
        mailing = self.env['mailing.mailing'].create({
            'name': 'mailing',
            'subject': 'some subject',
            'mailing_model_id': self.env['ir.model']._get('res.partner').id,
        })
        # create a schedule date wizard
        wizard_form = Form(
            self.env['mailing.mailing.schedule.date'].with_context(default_mass_mailing_id=mailing.id))

        # set a schedule date
        wizard_form.schedule_date = datetime(2021, 4, 30, 9, 0)
        wizard = wizard_form.save()
        wizard.action_schedule_date()

        # assert that the schedule_date and schedule_type fields are correct and that the mailing is put in queue
        self.assertEqual(mailing.schedule_date, datetime(2021, 4, 30, 9, 0))
        self.assertEqual(mailing.schedule_type, 'scheduled')
        self.assertEqual(mailing.state, 'in_queue')
