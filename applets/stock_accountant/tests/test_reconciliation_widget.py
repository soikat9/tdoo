# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.stock_account.tests.test_anglo_saxon_valuation_reconciliation_common import ValuationReconciliationTestCommon
from tele.tests.common import tagged


@tagged("post_install", "-at_install")
class TestReconciliationWidget(ValuationReconciliationTestCommon):

    def test_no_stock_account_in_reconciliation_proposition(self):
        """
        We check if no stock interim account is present in the reconcialiation proposition,
        with both standard and custom stock accounts
        """
        avco_1 = self.stock_account_product_categ.copy({'property_cost_method': 'average'})

        # We need a product category with custom stock accounts
        avco_2 = self.stock_account_product_categ.copy({
            'property_cost_method': 'average',
            'property_stock_account_input_categ_id': self.company_data['default_account_stock_in'].copy().id,
            'property_stock_account_output_categ_id': self.company_data['default_account_stock_out'].copy().id,
            'property_stock_journal': avco_1.property_stock_journal.copy(),
            'property_stock_valuation_account_id': self.company_data['default_account_stock_valuation'].copy().id
        })

        move_1, move_2 = self.env['account.move'].create([
            {
                'move_type': 'entry',
                'name': 'Entry 1',
                'journal_id': avco_1.property_stock_journal.id,
                'line_ids': [
                    (0, 0, {
                        'account_id': avco_1.property_stock_account_input_categ_id.id,
                        'debit': 0.0,
                        'credit': 100.0
                    }),
                    (0, 0, {
                        'account_id': avco_1.property_stock_valuation_account_id.id,
                        'debit': 100.0,
                        'credit': 0.0
                    })
                ]
            },
            {
                'move_type': 'entry',
                'name': 'Entry 2',
                'journal_id': avco_2.property_stock_journal.id,
                'line_ids': [
                    (0, 0, {
                        'account_id': avco_2.property_stock_account_input_categ_id.id,
                        'debit': 0.0,
                        'credit': 100.0
                    }),
                    (0, 0, {
                        'account_id': avco_2.property_stock_valuation_account_id.id,
                        'debit': 100.0,
                        'credit': 0.0
                    })
                ]
            },
        ])

        (move_1 + move_2).action_post()

        statement = self.env['account.bank.statement'].create({
            'journal_id': self.company_data['default_journal_bank'].id,
            'balance_start': 0.0,
            'balance_end': -100.0,
            'balance_end_real': -100.0,
            'line_ids': [(0, 0, {'payment_ref': 'test', 'amount': -100.0})]
        })

        statement.button_post()

        res = self.env['account.reconciliation.widget'].get_move_lines_for_bank_statement_line(statement.line_ids.id)
        stock_accounts_code = (
            avco_1.property_stock_account_input_categ_id + avco_2.property_stock_account_input_categ_id
            + avco_1.property_stock_account_output_categ_id + avco_2.property_stock_account_output_categ_id
        ).mapped('code')
        stock_res = [line for line in res if line['account_code'] in stock_accounts_code]
        self.assertEqual(len(stock_res), 0)
