# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.sale.tests.common import TestSaleCommonBase
from tele.applets.mail.tests.common import mail_new_test_user
from datetime import datetime


# This test class has to be tested at install since the flow is modified in industry_fsm_stock
# where the SO gets confirmed as soon as a product is added in an FSM task which causes the
# tests of this class to fail
class TestMultiCompanyCommon(TestSaleCommonBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # adding groups to users to use through the various tests
        user_group_employee = cls.env.ref('base.group_user')
        user_project_group_employee = cls.env.ref('project.group_project_user')

        cls.env.user.groups_id |= user_group_employee
        cls.env.user.groups_id |= user_project_group_employee
        cls.env.user.groups_id |= cls.env.ref('analytic.group_analytic_accounting')

        cls.companyA = cls.env['res.company'].create({'name': 'test_company_A'})
        cls.companyB = cls.env['res.company'].create({'name': 'test_company_B'})

        cls.user_employee_company_B = mail_new_test_user(
            cls.env,
            name='Gregor Clegane Employee',
            login='gregor',
            email='gregor@example.com',
            notification_type='email',
            groups='base.group_user',
            company_id=cls.companyB.id,
            company_ids=cls.companyB.ids,
        )
        cls.user_employee_company_B.write({
            'groups_id': [(6, 0, [user_group_employee.id, user_project_group_employee.id])],
        })
        cls.user_manager_company_B = mail_new_test_user(
            cls.env,
            name='Cersei Lannister Manager',
            login='cersei',
            email='cersei@example.com',
            notification_type='email',
            groups='base.group_user',
            company_id=cls.companyB.id,
            company_ids=cls.companyB.ids,
        )
        cls.user_manager_company_B.sudo().write({
            'groups_id': [(6, 0, [user_group_employee.id, user_project_group_employee.id])],
        })
        Project = cls.env['project.project'].sudo().with_context({'mail_create_nolog': True, 'tracking_disable': True})
        cls.fsm_company_a = Project.create({
            'name': 'FSM Company A',
            'alias_name': 'fsm+companya',
            'company_id': cls.env.company.id,
            'is_fsm': True,
            'allow_timesheets': True,
            'allow_billable': True,
            'timesheet_product_id': cls.env.ref('sale_timesheet.time_product').id,
            'allow_material': True,
            'allow_quotations': True,
            'type_ids': [
                (0, 0, {
                    'name': 'New',
                    'sequence': 1,
                }),
                (0, 0, {
                    'name': 'Won',
                    'sequence': 10,
                })
            ]
        })

        cls.default_user_employee = cls.env['res.users'].create({
            'name': 'default_user_employee',
            'login': 'default_user_employee.comp%s' % cls.companyA.id,
            'email': 'default_user_employee@example.com',
            'groups_id': [(6, 0, [cls.env.ref('base.group_user').id])],
            'company_ids': cls.companyA.ids,
            'company_id': cls.companyA.id,
        })
        cls.partner_a = cls.env['res.partner'].create({
            'name': 'partner_a',
            'company_id': False,
        })

        Task = cls.env['project.task'].with_context({'mail_create_nolog': True, 'tracking_disable': True})
        cls.task_1 = Task.create({
            'name': 'Task 1 in Project A',
            'user_ids': cls.default_user_employee.ids,
            'partner_id': cls.partner_a.id,
            'project_id': cls.fsm_company_a.id
        })

        cls.task_2 = Task.create({
            'name': 'Task 2 in Project A',
            'user_ids': cls.default_user_employee.ids,
            'partner_id': cls.partner_a.id,
            'project_id': cls.fsm_company_a.id
        })

        values = {
            'task_id': cls.task_1.id,
            'project_id': cls.task_1.project_id.id,
            'date': datetime.now(),
            'name': 'test timesheet',
            'user_id': cls.default_user_employee.id,
            'unit_amount': 0.25,
        }
        cls.env['account.analytic.line'].create(values)

    def test_task(self):
        # This should not raise an error.
        self.task_1.with_context(allowed_company_ids=[self.env.company.id, self.companyB.id], company_id=self.companyB.id).action_fsm_view_material()

        self.assertFalse(self.task_1.fsm_done, "Task should not be validated")
        self.assertFalse(self.task_1.sale_order_id, "Task should not be linked to a SO")
        self.task_1._fsm_ensure_sale_order()
        self.assertEqual(self.task_1.sale_order_id.state, 'draft', "Sale order should not be confirmed")
        # Validating a task while in another company should not impact the propagation of the company_id to the sale order
        self.task_1.with_context(allowed_company_ids=[self.env.company.id, self.companyB.id], company_id=self.companyB.id).action_fsm_validate()
        self.assertTrue(self.task_1.fsm_done, "Task should be validated")
        self.assertEqual(self.task_1.sale_order_id.state, 'sale', "Sale order should be confirmed")
        self.assertEqual(self.task_1.sale_order_id.company_id.id, self.task_1.company_id.id, "The company of the sale order should be the same as the one from the task")
        # Generating an invoice from a task while in another company should not impact the propagation of the company_id to the invoice
        self.assertTrue(self.task_1.task_to_invoice, "Task should be invoiceable")
        # YTI This is supposed to be reintroduced after a fix from DBO See #42408
        # invoice_ctx = self.task_1.action_create_invoice()['context']
        # invoice_ctx['allowed_company_ids']=[self.env.company.id, self.company_data_2['company'].id]
        # invoice_ctx['company_id']=self.company_data_2['company'].id
        # invoice_wizard = self.env['sale.advance.payment.inv'].with_context(invoice_ctx).create({})
        # invoice_wizard.create_invoices()
        # self.assertFalse(self.task_1.task_to_invoice, "Task should not be invoiceable")
        # self.assertEqual(self.task_1.sale_order_id.invoice_ids[0].company_id.id, self.task_1.company_id.id, "The company of the invoice should be the same as the one from the task")
