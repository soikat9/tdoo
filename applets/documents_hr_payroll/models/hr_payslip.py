# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class HrPaylsip(models.Model):
    _name = 'hr.payslip'
    _inherit = ['hr.payslip', 'documents.mixin']

    def _get_document_tags(self):
        return self.company_id.documents_hr_payslips_tags

    def _get_document_owner(self):
        return self.employee_id.user_id

    def _get_document_partner(self):
        return self.employee_id.address_home_id

    def _get_document_folder(self):
        return self.company_id.documents_payroll_folder_id

    def _check_create_documents(self):
        return self.company_id.documents_hr_settings and super()._check_create_documents()
