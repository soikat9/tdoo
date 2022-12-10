# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models


class HrDepartureWizard(models.TransientModel):
    _inherit = 'hr.departure.wizard'

    release_campany_car = fields.Boolean("Release Company Car", default=True,
        help="Release the company car.")

    def action_register_departure(self):
        super(HrDepartureWizard, self).action_register_departure()
        if self.release_campany_car:
            self._free_campany_car()

    def _free_campany_car(self):
        """Find all automotive.vehichle.assignation.log records that link to the employee, if there is no 
        end date or end date > departure date, update the date. Also check automotive.vehicle to see if 
        there is any record with its dirver_id to be the employee, set them to False."""
        drivers = self.employee_id.user_id.partner_id | self.employee_id.sudo().address_home_id
        assignations = self.env['automotive.vehicle.assignation.log'].search([('driver_id', 'in', drivers.ids)])
        for assignation in assignations:
            if self.departure_date and (not assignation.date_end or assignation.date_end > self.departure_date):
                assignation.write({'date_end': self.departure_date})
        cars = self.env['automotive.vehicle'].search([('driver_id', 'in', drivers.ids)])
        cars.write({'driver_id': False, 'driver_employee_id': False})
