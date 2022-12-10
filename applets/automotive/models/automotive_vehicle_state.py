# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class AutomotiveVehicleState(models.Model):
    _name = 'automotive.vehicle.state'
    _order = 'sequence asc'
    _description = 'Vehicle Status'

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer(help="Used to order the note stages")

    _sql_constraints = [('automotive_state_name_unique', 'unique(name)', 'State name already exists')]
