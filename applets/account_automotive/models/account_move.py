# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _post(self, soft=True):
        vendor_bill_service = self.env.ref('account_automotive.data_automotive_service_type_vendor_bill', raise_if_not_found=False)
        if not vendor_bill_service:
            return super()._post(soft)

        val_list = []
        log_list = []
        not_posted_before = self.filtered(lambda r: not r.posted_before)
        posted = super()._post(soft)  # We need the move name to be set, but we also need to know which move are posted for the first time.
        for line in (not_posted_before & posted).line_ids.filtered(lambda ml: ml.vehicle_id and ml.move_id.move_type == 'in_invoice'):
            val = line._prepare_automotive_log_service()
            log = _('Service Vendor Bill: <a href=# data-oe-model=account.move data-oe-id={move_id}>{move_name}</a>').format(
                move_id=line.move_id.id,
                move_name=line.move_id.name,
            )
            val_list.append(val)
            log_list.append(log)
        log_service_ids = self.env['automotive.vehicle.log.services'].create(val_list)
        for log_service_id, log in zip(log_service_ids, log_list):
            log_service_id.message_post(body=log)
        return posted


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    vehicle_id = fields.Many2one('automotive.vehicle', string='Vehicle', index=True)
    need_vehicle = fields.Boolean(compute='_compute_need_vehicle',
        help="Technical field to decide whether the vehicle_id field is editable")

    def _compute_need_vehicle(self):
        self.need_vehicle = False

    def _prepare_automotive_log_service(self):
        vendor_bill_service = self.env.ref('account_automotive.data_automotive_service_type_vendor_bill', raise_if_not_found=False)
        return {
            'service_type_id': vendor_bill_service.id,
            'vehicle_id': self.vehicle_id.id,
            'amount': self.price_subtotal,
            'vendor_id': self.partner_id.id,
            'description': self.name,
        }
