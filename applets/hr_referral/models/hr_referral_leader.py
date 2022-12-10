# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class HrReferralLeader(models.Model):
    _name = 'hr.referral.leader'
    _description = 'Leaders for Referrals'

    name = fields.Char('Leader Name', required=True)
    position = fields.Selection([
        ('front', 'Front'),
        ('back', 'Back')
    ], required=True, default='back', help="Define the position of the leader. If it's a small leader like a dog, you must select Front, it will be placed in the front of the dashboard, above superhero.")
    image = fields.Binary("Dashboard Image", required=True,
        help="This field holds the image used as image for the leader on the dashboard, limited to 1024x1024px.")
    image_head = fields.Binary("Image", required=True,
        help="This field holds the image used as image for the head's leader when the user must choose a new leader, limited to 1024x1024px.")
