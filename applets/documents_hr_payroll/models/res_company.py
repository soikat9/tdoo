# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    def _domain_company(self):
        company = self.env.company
        return ['|', ('company_id', '=', False), ('company_id', '=', company.id)]

    documents_hr_payslips_tags = fields.Many2many('documents.tag', 'payslip_tags_table')
    documents_payroll_folder_id = fields.Many2one('documents.folder', domain=_domain_company,
                                          default=lambda self: self.env.ref('documents_hr_payroll.documents_payroll_folder', raise_if_not_found=False))
