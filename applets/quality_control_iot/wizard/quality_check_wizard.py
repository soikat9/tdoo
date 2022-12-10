# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class QualityCheckWizard(models.TransientModel):

    _inherit = 'quality.check.wizard'

    ip = fields.Char(related='current_check_id.ip')
    identifier = fields.Char(related='current_check_id.identifier')
