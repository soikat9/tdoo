# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class StockLocation(models.Model):
    _inherit = 'stock.location'

    amazon_location = fields.Boolean(
        help="True if this location represents the stock of a seller managed by Amazon under the "
             "Amazon Fulfillment program", default=False)
