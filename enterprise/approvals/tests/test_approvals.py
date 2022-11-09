# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields
from tele.tests import common
from tele.exceptions import UserError


class TestRequest(common.TransactionCase):
    def test_compute_request_status(self):
        category_test = self.env['approval.category'].browse(1)
        record = self.env['approval.request'].create({
            'name': 'test request',
            'category_id': category_test.id,
            'date_start': fields.Datetime.now(),
            'date_end': fields.Datetime.now(),
            'location': 'testland'
        })
        first_approver = self.env['approval.approver'].create({
            'user_id': 1,
            'request_id': record.id,
            'status': 'new'})
        second_approver = self.env['approval.approver'].create({
            'user_id': 2,
            'request_id': record.id,
            'status': 'new'})
        record.approver_ids = (first_approver | second_approver)

        self.assertEqual(record.request_status, 'new')

        record.action_confirm()

        # Test case 1: Min approval = 1
        self.assertEqual(record.request_status, 'pending')
        record.action_approve(first_approver)
        self.assertEqual(record.request_status, 'approved')
        record.action_approve(second_approver)
        self.assertEqual(record.request_status, 'approved')
        record.action_withdraw(first_approver)
        self.assertEqual(record.request_status, 'approved')
        record.action_refuse(first_approver)
        self.assertEqual(record.request_status, 'refused')

        # Test case 2: Min approval = 1
        category_test.approval_minimum = 2
        record.action_withdraw(first_approver)
        record.action_withdraw(second_approver)
        self.assertEqual(record.request_status, 'pending')
        record.action_approve(first_approver)
        self.assertEqual(record.request_status, 'pending')
        record.action_approve(second_approver)
        self.assertEqual(record.request_status, 'approved')
        record.action_withdraw(second_approver)
        self.assertEqual(record.request_status, 'pending')
        record.action_refuse(second_approver)
        self.assertEqual(record.request_status, 'refused')

        # Test case 3: Check that cancel is erasing the old validations
        record.action_cancel()
        self.assertEqual(first_approver.status, 'cancel')
        self.assertEqual(second_approver.status, 'cancel')
        self.assertEqual(record.request_status, 'cancel')

        # Test case 4: Set the approval request to draft
        record.action_draft()
        self.assertEqual(first_approver.status, 'new')
        self.assertEqual(second_approver.status, 'new')
        self.assertEqual(record.request_status, 'new')

        # Test case 5: Set min approval to an impossible value to reach
        category_test.approval_minimum = 3
        with self.assertRaises(UserError):
            record.action_confirm()
        self.assertEqual(record.request_status, 'new')

    def test_compute_request_status_with_required(self):
        category_test = self.env['approval.category'].browse(1)
        record = self.env['approval.request'].create({
            'name': 'test request',
            'category_id': category_test.id,
            'date_start': fields.Datetime.now(),
            'date_end': fields.Datetime.now(),
            'location': 'testland'
        })
        first_approver = self.env['approval.approver'].create({
            'user_id': 1,
            'request_id': record.id,
            'status': 'new',
            'required': True})
        second_approver = self.env['approval.approver'].create({
            'user_id': 2,
            'request_id': record.id,
            'status': 'new'})
        record.approver_ids = (first_approver | second_approver)

        self.assertEqual(record.request_status, 'new')

        record.action_confirm()

        # Min approval = 1 but first approver IS required
        self.assertEqual(record.request_status, 'pending')
        record.action_approve(second_approver)
        # Min approval is met but required approvals are not
        self.assertEqual(record.request_status, 'pending')
        record.action_approve(first_approver)
        self.assertEqual(record.request_status, 'approved')

        # Min approval = 2
        category_test.approval_minimum = 2
        record.action_withdraw(first_approver)
        record.action_withdraw(second_approver)
        self.assertEqual(record.request_status, 'pending')
        record.action_approve(first_approver)
        # All required approvals are met but not the minimal approval count
        self.assertEqual(record.request_status, 'pending')
        record.action_approve(second_approver)
        self.assertEqual(record.request_status, 'approved')
