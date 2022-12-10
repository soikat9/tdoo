# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class AutomotiveServiceType(models.Model):
    _name = 'automotive.service.type'
    _description = 'Automotive Service Type'

    name = fields.Char(required=True, translate=True)
    category = fields.Selection([
        ('contract', 'Contract'),
        ('service', 'Service')
        ], 'Category', required=True, help='Choose whether the service refer to contracts, vehicle services or both')
