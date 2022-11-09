# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    schedule_count = fields.Integer('Schedules', compute='_compute_schedule_count')

    def _compute_schedule_count(self):
        for rec in self:
            rec.schedule_count = self.env['mrp.production.schedule'].search_count([
                ('product_id.product_tmpl_id', '=', rec.id)])

    def action_open_mps_view(self):
        action = self.env["ir.actions.actions"]._for_xml_id("mrp_mps.action_mrp_mps")
        action['context'] = {"search_default_product_id": self.product_variant_ids.ids}
        return action
