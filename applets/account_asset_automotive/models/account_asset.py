# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models, _
from tele.exceptions import UserError


class AccountAsset(models.Model):
    _inherit = 'account.asset'

    vehicle_id = fields.Many2one('automotive.vehicle', compute='_compute_vehicle_id')

    @api.onchange('original_move_line_ids')
    def _compute_vehicle_id(self):
        for record in self:
            if len(record.original_move_line_ids.vehicle_id) > 1:
                raise UserError(_("All the lines should be from the same vehicle"))
            record.vehicle_id = record.original_move_line_ids.vehicle_id

    def action_open_vehicle(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'automotive.vehicle',
            'res_id': self.vehicle_id.id,
            'view_ids': [(False, 'form')],
            'view_mode': 'form',
        }
