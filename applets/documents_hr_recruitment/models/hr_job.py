# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class HrJob(models.Model):
    _name = 'hr.job'
    _inherit = ['hr.job', 'documents.mixin']

    def _get_document_folder(self):
        return self.company_id.recruitment_folder_id

    def _check_create_documents(self):
        return self.company_id.documents_recruitment_settings and super()._check_create_documents()
