# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class SocialPost(models.Model):
    _inherit = "social.post"

    event_track_id = fields.Many2one('event.track', string="Linked Event Track",
        help="Technical field that holds the relationship between a track and this 'reminder' post",
        ondelete='cascade')
