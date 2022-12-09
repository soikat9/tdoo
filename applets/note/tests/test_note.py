# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.base.tests.common import TransactionCaseWithUserDemo


class TestNote(TransactionCaseWithUserDemo):

    def test_bug_lp_1156215(self):
        """ ensure any users can create new users """
        demo_user = self.user_demo
        group_erp = self.env.ref('base.group_tele_manager')

        demo_user.write({
            'groups_id': [(4, group_erp.id)],
        })

        # must not fail
        demo_user.create({
            'name': 'test bug lp:1156215',
            'login': 'lp_1156215',
        })
