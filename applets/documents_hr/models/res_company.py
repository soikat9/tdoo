# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    def _domain_company(self):
        company = self.env.company
        return ['|', ('company_id', '=', False), ('company_id', '=', company.id)]

    documents_hr_settings = fields.Boolean()
    documents_hr_folder = fields.Many2one('documents.folder', string="hr Workspace", domain=_domain_company,
                                          default=lambda self: self.env.ref('documents_hr.documents_hr_folder',
                                                                            raise_if_not_found=False))
