# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def _domain_company(self):
        company = self.env.company
        return ['|', ('company_id', '=', False), ('company_id', '=', company.id)]

    deferred_time_off_manager = fields.Many2one('res.users', related='company_id.deferred_time_off_manager', domain=_domain_company, readonly=False)
