# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class Partner(models.Model):
    _inherit = 'res.partner'
    _mailing_enabled = True
