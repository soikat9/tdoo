# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.tests import Form

from .test_common import TestQualityMrpCommon

class TestQualityCheck(TestQualityMrpCommon):

    def test_00_production_quality_check(self):

        """Test quality check on production order."""

        # Create Quality Point for product Laptop Customized with Manufacturing Operation Type.
        self.qality_point_test1 = self.env['quality.point'].create({
            'product_ids': [(4, self.product_id)],
            'picking_type_ids': [(4, self.picking_type_id)],
        })

        # Check that quality point created.
        assert self.qality_point_test1, "First Quality Point not created for Laptop Customized."

        # Create Production Order of Laptop Customized to produce 5.0 Unit.
        production_form = Form(self.env['mrp.production'])
        production_form.product_id = self.env['product.product'].browse(self.product_id)
        production_form.product_qty = 5.0
        self.mrp_production_qc_test1 = production_form.save()

        # Check that Production Order of Laptop Customized to produce 5.0 Unit is created.
        assert self.mrp_production_qc_test1, "Production Order not created."

        # Perform check availability and produce product.
        self.mrp_production_qc_test1.action_confirm()
        self.mrp_production_qc_test1.action_assign()

        mo_form = Form(self.mrp_production_qc_test1)
        mo_form.qty_producing = self.mrp_production_qc_test1.product_qty
        mo_form.lot_producing_id = self.lot_product_27_0
        details_operation_form = Form(self.mrp_production_qc_test1.move_raw_ids[0], view=self.env.ref('stock.view_stock_move_operations'))
        with details_operation_form.move_line_ids.new() as ml:
            ml.qty_done = self.mrp_production_qc_test1.product_qty
        details_operation_form.save()

        self.mrp_production_qc_test1 = mo_form.save()
        # Check Quality Check for Production is created and check it's state is 'none'.
        self.assertEqual(len(self.mrp_production_qc_test1.check_ids), 1)
        self.assertEqual(self.mrp_production_qc_test1.check_ids.quality_state, 'none')

        # 'Pass' Quality Checks of production order.
        self.mrp_production_qc_test1.check_ids.do_pass()

        # Set MO Done.
        self.mrp_production_qc_test1.button_mark_done()

        # Now check state of quality check.
        self.assertEqual(self.mrp_production_qc_test1.check_ids.quality_state, 'pass')

    def test_01_production_quality_check_product(self):
        """ Test quality check on production order with type product for tracked and non-tracked manufactured product
        """

        product_without_tracking = self.env['product.product'].create({
            'name': 'Product not tracked',
            'type': 'product',
            'tracking': 'none',
        })

        # Create Quality Point for product Drawer with Manufacturing Operation Type.
        self.env['quality.point'].create({
            'product_ids': [self.product_id],
            'picking_type_ids': [self.picking_type_id],
            'measure_on': 'product',
            'is_lot_tested_fractionally': True,
            'testing_percentage_within_lot': 50,
        })
        # Create Quality Point for component Drawer Case Black with Manufacturing Operation Type.
        self.env['quality.point'].create({
            'product_ids': [self.product.bom_ids.bom_line_ids[0].product_id.id],
            'picking_type_ids': [self.picking_type_id],
            'measure_on': 'product',
        })
        # Create Quality Point for all products with Manufacturing Operation Type.
        # This should apply for all products but not to the components of a MO
        self.env['quality.point'].create({
            'picking_type_ids': [self.picking_type_id],
            'measure_on': 'product',
        })

        # Create Production Order of Drawer to produce 5.0 Unit.
        production_form = Form(self.env['mrp.production'])
        production_form.product_id = self.product
        production_form.product_qty = 5.0
        production = production_form.save()
        production.action_confirm()
        production.qty_producing = 4.0
        production.action_generate_serial()

        # Check that the Quality Check were created and has correct values
        self.assertEqual(len(production.move_raw_ids[0].move_line_ids.check_ids), 1)
        self.assertEqual(len(production.check_ids), 3)
        self.assertEqual(production.check_ids.filtered(lambda qc: qc.product_id == production.product_id)[0].qty_to_test, 2)

        # Create Production Order of non-tracked product
        production2_form = Form(self.env['mrp.production'])
        production2_form.product_id = product_without_tracking
        production2 = production2_form.save()
        production2.action_confirm()
        production2.qty_producing = 1.0

        # Check that the Quality Check was created
        self.assertEqual(len(production2.check_ids), 1)

    def test_01_quality_check_scrapped(self):
        """
        Test that when scrapping a manufacturing order, no quality check is created for that move
        """
        product = self.env['product.product'].create({'name': 'Time'})
        component = self.env['product.product'].create({'name': 'Money'})

        # Create a quality point for Manufacturing on All Operations (All Operations is set by default)
        qp = self.env['quality.point'].create({'picking_type_ids': [(4, self.picking_type_id)]})
        # Create a Manufacturing order for a product
        mo_form = Form(self.env['mrp.production'])
        mo_form.product_id = product
        mri_form = mo_form.move_raw_ids.new()
        mri_form.product_id = component
        mri_form.product_uom_qty = 1
        mri_form.save()
        mo = mo_form.save()
        mo.action_confirm()
        # Delete the created quality check
        qc = self.env['quality.check'].search([('product_id', '=', product.id), ('point_id', '=', qp.id)])
        qc.unlink()

        # Scrap the Manufacturing Order
        scrap = self.env['stock.scrap'].with_context(active_model='mrp.production', active_id=mo.id).create({
            'product_id': product.id,
            'scrap_qty': 1.0,
            'product_uom_id': product.uom_id.id,
            'production_id': mo.id
        })
        scrap.do_scrap()
        self.assertEqual(len(self.env['quality.check'].search([('product_id', '=', product.id), ('point_id', '=', qp.id)])), 0, "Quality checks should not be created for scrap moves")
