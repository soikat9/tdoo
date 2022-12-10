# -*- coding:utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


from tele import fields, models


class HrJob(models.Model):
    _inherit = 'hr.job'

    default_contract_id = fields.Many2one('hr.contract', domain="[('company_id', '=', company_id), ('employee_id', '=', False)]", string="Contract Template",
        help="Default contract used when making an offer to an applicant.")
