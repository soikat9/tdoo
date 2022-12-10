# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    registration_ids = fields.One2many('event.registration', 'partner_id', string='Event Registrations')
