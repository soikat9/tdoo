# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class ProjectProject(models.Model):
    _name = 'project.project'
    _inherit = ['project.project', 'documents.mixin']

    def _get_document_tags(self):
        return self.company_id.project_tags

    def _get_document_folder(self):
        return self.company_id.project_folder

    def _check_create_documents(self):
        return self.company_id.documents_project_settings and super()._check_create_documents()
