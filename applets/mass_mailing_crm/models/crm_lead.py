# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _mailing_enabled = True
