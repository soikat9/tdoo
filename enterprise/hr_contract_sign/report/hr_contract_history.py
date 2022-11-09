# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models, fields, _


class HrContract(models.Model):
    _inherit = 'hr.contract.history'

    sign_request_ids = fields.Many2many('sign.request', string='Requested Signatures')

    def action_sign_contract_wizard(self):
        self.ensure_one()
        action = self.env['ir.actions.actions']._for_xml_id('hr_contract_sign.sign_contract_wizard_action')
        action['context'] = {'active_id': self.contract_id.id}
        return action
