# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class AutomotiveVehicleAssignationLog(models.Model):
    _name = "automotive.vehicle.assignation.log"
    _description = "Drivers history on a vehicle"
    _order = "create_date desc, date_start desc"

    vehicle_id = fields.Many2one('automotive.vehicle', string="Vehicle", required=True)
    driver_id = fields.Many2one('res.partner', string="Driver", required=True)
    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string="End Date")
