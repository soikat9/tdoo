# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    image_fetch_pending = fields.Boolean(
        help="Whether an image must be fetched for this product. Handled by a cron.",
    )
