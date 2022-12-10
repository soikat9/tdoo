# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    amazon_team = fields.Boolean(
        help="True if this sales team is associated with Amazon orders", default=False)
