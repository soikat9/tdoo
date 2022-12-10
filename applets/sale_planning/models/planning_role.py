# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models

class PlanningRole(models.Model):
    _inherit = 'planning.role'

    product_ids = fields.One2many('product.template', 'planning_role_id', string='Services', domain=[('type', '=', 'service'), ('sale_ok', '=', True)])
