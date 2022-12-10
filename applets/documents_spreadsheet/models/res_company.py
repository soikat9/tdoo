# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    def _spreadsheet_folder_domain(self):
        return ['|', ('company_id', '=', False), ('company_id', '=', self.env.company.id)]

    documents_spreadsheet_folder_id = fields.Many2one('documents.folder', domain=_spreadsheet_folder_domain,
        default=lambda self: self.env.ref('documents_spreadsheet.documents_spreadsheet_folder', raise_if_not_found=False))
