# -*- coding: utf-8 -*-
# Part of Tele. See LICENSE file for full copyright and licensing details.

from tele import api, fields, models, Command


class MrpEco(models.Model):
    _inherit = 'mrp.eco'

    @api.depends(
        'bom_id.operation_ids.quality_point_ids',
        'new_bom_id.operation_ids.quality_point_ids',
        'bom_id.operation_ids.quality_point_ids.test_type_id',
        'new_bom_id.operation_ids.quality_point_ids.test_type_id')
    def _compute_routing_change_ids(self):
        return super()._compute_routing_change_ids()

    def _prepare_detailed_change_commands(self, new_op, old_op):
        commands = []
        new_points = new_op.quality_point_ids
        new_point_dict = dict((p.title, p) for p in new_points)
        if old_op:
            for old_point in old_op.quality_point_ids:
                new_point = new_point_dict.get(old_point.title, False)
                if new_point:
                    del new_point_dict[old_point.title]
                    if old_point.test_type_id == new_point.test_type_id:
                        continue
                    else:
                        commands += [Command.create({
                            'change_type': 'update',
                            'workcenter_id': new_op.workcenter_id.id,
                            'operation_id': new_op.id,
                            'quality_point_id': new_point.id,
                        })]
                else:
                    commands += [Command.create({
                        'change_type': 'remove',
                        'workcenter_id': old_op.workcenter_id.id,
                        'operation_id': old_op.id,
                        'quality_point_id': old_point.id,
                    })]
        for new_point in new_point_dict.values():
            commands += [Command.create({
                'change_type': 'add',
                'workcenter_id': new_op.workcenter_id.id,
                'operation_id': new_op.id,
                'quality_point_id': new_point.id,
            })]
        return commands


class MrpEcoRoutingChange(models.Model):
    _inherit = 'mrp.eco.routing.change'

    quality_point_id = fields.Many2one('quality.point')
    step = fields.Char(related='quality_point_id.name', string='Step')
    test_type = fields.Many2one('quality.point.test_type', related='quality_point_id.test_type_id', string='Step Type')
