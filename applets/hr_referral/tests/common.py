# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.tests.common import TransactionCase

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestHrReferralBase(TransactionCase):

    def setUp(self):
        super(TestHrReferralBase, self).setUp()

        self.company_1 = self.env['res.company'].create({'name': 'Opoo'})
        self.company_2 = self.env['res.company'].create({'name': 'Otoo'})
        self.company_ids = [self.company_1.id, self.company_2.id]

        self.dep_rd = self.env['hr.department'].create({
            'name': 'Research and Development',
            'company_id': self.company_1.id
        })

        # I create a new user "Richard"
        self.richard_user = self.env['res.users'].create({
            'name': 'Richard',
            'login': 'ric'
        })

        # I create a new user "Steve"
        self.steve_user = self.env['res.users'].create({
            'name': 'Steve',
            'login': 'stv'
        })

        self.job_dev = self.env['hr.job'].create({
            'name': 'Dev',
            'no_of_recruitment': '5',
            'department_id': self.dep_rd.id,
            'company_id': self.company_1.id,
        })

        self.contract_promotion = self.env['hr.referral.reward'].create({
            'name': 'Contract Promotion',
            'description': 'Beautiful and usefull',
            'cost': '5',
            'company_id': self.company_1.id,
        })

        self.red_contract_promotion = self.env['hr.referral.reward'].create({
            'name': 'Red Contract Promotion',
            'description': 'It\'s red',
            'cost': '10',
            'company_id': self.company_2.id,
        })

        self.contract_promotion = self.contract_promotion.with_user(self.richard_user.id)

        def _get_title_from_url(u):
            return "Hello"

        patcher = patch('tele.applets.link_tracker.models.link_tracker.LinkTracker._get_title_from_url', wraps=_get_title_from_url)
        patcher.start()
        self.addCleanup(patcher.stop)
