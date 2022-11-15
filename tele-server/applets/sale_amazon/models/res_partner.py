# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    amazon_email = fields.Char(help="The encrypted email of the customer. Does not forward mails")
