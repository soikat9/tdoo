# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


class Challenge(models.Model):
    _inherit = 'recognition.challenge'

    challenge_category = fields.Selection(selection_add=[
        ('slides', 'Website / Slides')
    ], ondelete={'slides': 'set default'})
