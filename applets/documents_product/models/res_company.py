# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models, api, _


class ResCompany(models.Model):
    _inherit = "res.company"

    def _domain_company(self):
        company = self.env.company
        return ['|', ('company_id', '=', False), ('company_id', '=', company.id)]

    documents_product_settings = fields.Boolean()
    product_folder = fields.Many2one('documents.folder', string="Product Workspace", domain=_domain_company,
                                     default=lambda self: self.env.ref('documents_product_folder',
                                                                       raise_if_not_found=False))
    product_tags = fields.Many2many('documents.tag', 'product_tags_table')
