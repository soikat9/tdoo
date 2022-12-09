# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class SponsorType(models.Model):
    _name = "event.sponsor.type"
    _description = 'Event Sponsor Level'
    _order = "sequence"

    def _default_sequence(self):
        return (self.search([], order="sequence desc", limit=1).sequence or 0) + 1

    name = fields.Char('Sponsor Level', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=_default_sequence)
    display_ribbon_style = fields.Selection(
        [('no_ribbon', 'No Ribbon'), ('Gold', 'Gold'),
         ('Silver', 'Silver'), ('Bronze', 'Bronze')],
        string='Ribbon Style', default='no_ribbon')
