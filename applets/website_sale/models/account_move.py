# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    website_id = fields.Many2one('website', related='partner_id.website_id', string='Website',
                                 help='Website through which this invoice was created.',
                                 store=True, readonly=True, tracking=True)
