# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class AutomotiveVehicleAssignationLog(models.Model):
    _inherit = 'automotive.vehicle.assignation.log'

    driver_employee_id = fields.Many2one(related="vehicle_id.driver_employee_id", string='Driver (Employee)')
    attachment_number = fields.Integer('Number of Attachments', compute='_compute_attachment_number')

    def _compute_attachment_number(self):
        attachment_data = self.env['ir.attachment'].read_group([
            ('res_model', '=', 'automotive.vehicle.assignation.log'),
            ('res_id', 'in', self.ids)], ['res_id'], ['res_id'])
        attachment = dict((data['res_id'], data['res_id_count']) for data in attachment_data)
        for doc in self:
            doc.attachment_number = attachment.get(doc.id, 0)

    def action_get_attachment_view(self):
        self.ensure_one()
        res = self.env['ir.actions.act_window']._for_xml_id('base.action_attachment')
        res['domain'] = [('res_model', '=', 'automotive.vehicle.assignation.log'), ('res_id', 'in', self.ids)]
        res['context'] = {'default_res_model': 'automotive.vehicle.assignation.log', 'default_res_id': self.id}
        return res
