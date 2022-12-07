# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    is_expired = fields.Boolean(related='lot_id.product_expiry_alert')
