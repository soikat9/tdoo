# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models, _, exceptions


class grant_badge_wizard(models.TransientModel):
    """ Wizard allowing to grant a badge to a user"""
    _name = 'recognition.badge.user.wizard'
    _description = 'Recognition User Badge Wizard'

    user_id = fields.Many2one("res.users", string='User', required=True)
    badge_id = fields.Many2one("recognition.badge", string='Badge', required=True)
    comment = fields.Text('Comment')

    def action_grant_badge(self):
        """Wizard action for sending a badge to a chosen user"""

        BadgeUser = self.env['recognition.badge.user']

        uid = self.env.uid
        for wiz in self:
            if uid == wiz.user_id.id:
                raise exceptions.UserError(_('You can not grant a badge to yourself.'))

            #create the badge
            BadgeUser.create({
                'user_id': wiz.user_id.id,
                'sender_id': uid,
                'badge_id': wiz.badge_id.id,
                'comment': wiz.comment,
            })._send_badge()

        return True
