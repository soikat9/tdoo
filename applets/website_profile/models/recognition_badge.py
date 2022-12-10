# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class RecognitionBadge(models.Model):
    _name = 'recognition.badge'
    _inherit = ['recognition.badge', 'website.published.mixin']
