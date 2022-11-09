# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class HrReferralOnboarding(models.Model):
    _name = 'hr.referral.onboarding'
    _description = 'Welcome Onboarding in Referral App'
    _order = 'sequence'
    _rec_name = 'text'

    sequence = fields.Integer()
    text = fields.Text(required=True)
    image = fields.Binary(required=True)
    company_id = fields.Many2one('res.company', 'Company')
