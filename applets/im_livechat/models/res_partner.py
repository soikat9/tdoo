# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models, fields


class Partners(models.Model):
    """Update of res.partner class to take into account the livechat username."""
    _inherit = 'res.partner'

    user_livechat_username = fields.Char(compute='_compute_user_livechat_username')

    def _get_channels_as_member(self):
        channels = super()._get_channels_as_member()
        channels |= self.env['mail.channel'].search([
            ('channel_type', '=', 'livechat'),
            ('channel_last_seen_partner_ids', 'in', self.env['mail.channel.partner'].sudo()._search([
                ('partner_id', '=', self.id),
                ('is_pinned', '=', True),
            ])),
        ])
        return channels

    @api.depends('user_ids.livechat_username')
    def _compute_user_livechat_username(self):
        for partner in self:
            partner.user_livechat_username = next(iter(partner.user_ids.mapped('livechat_username')), False)
