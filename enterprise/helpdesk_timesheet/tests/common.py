# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.tests.common import TransactionCase


class TestHelpdeskTimesheetCommon(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.partner = cls.env['res.partner'].create({
            'name': 'Customer Task',
            'email': 'customer@task.com',
        })

        cls.analytic_account = cls.env['account.analytic.account'].create({
            'name': 'Analytic Account for Test Customer',
            'partner_id': cls.partner.id,
            'code': 'TEST',
        })

        cls.project = cls.env['project.project'].create({
            'name': 'Project',
            'allow_timesheets': True,
            'partner_id': cls.partner.id,
        })

        cls.helpdesk_team = cls.env['helpdesk.team'].create({
            'name': 'Test Team',
            'use_helpdesk_timesheet': True,
            'project_id': cls.project.id,
        })
