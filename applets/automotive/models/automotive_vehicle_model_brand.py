# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models


class AutomotiveVehicleModelBrand(models.Model):
    _name = 'automotive.vehicle.model.brand'
    _description = 'Brand of the vehicle'
    _order = 'name asc'

    name = fields.Char('Make', required=True)
    image_128 = fields.Image("Logo", max_width=128, max_height=128)
    model_count = fields.Integer(compute="_compute_model_count", string="", store=True)
    model_ids = fields.One2many('automotive.vehicle.model', 'brand_id')

    @api.depends('model_ids')
    def _compute_model_count(self):
        Model = self.env['automotive.vehicle.model']
        for record in self:
            record.model_count = Model.search_count([('brand_id', '=', record.id)])

    def action_brand_model(self):
        self.ensure_one()
        view = {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'automotive.vehicle.model',
            'name': 'Models',
            'context': {'search_default_brand_id': self.id, 'default_brand_id': self.id}
        }

        return view
