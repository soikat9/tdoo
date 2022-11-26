# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    documents_spreadsheet_folder_id = fields.Many2one(
        'documents.folder', related='company_id.documents_spreadsheet_folder_id', readonly=False)
