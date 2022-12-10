# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import _, fields, models
from tele.exceptions import UserError, ValidationError


class PaymentToken(models.Model):
    _inherit = 'payment.token'

    adyen_shopper_reference = fields.Char(
        string="Shopper Reference", help="The unique reference of the partner owning this token",
        readonly=True)

    #=== BUSINESS METHODS ===#

    def _handle_deactivation_request(self):
        """ Override of payment to request request Adyen to delete the token.

        Note: self.ensure_one()

        :return: None
        """
        super()._handle_deactivation_request()
        if self.provider != 'adyen':
            return

        data = {
            'merchantAccount': self.acquirer_id.adyen_merchant_account,
            'shopperReference': self.adyen_shopper_reference,
            'recurringDetailReference': self.acquirer_ref,
        }
        try:
            self.acquirer_id._adyen_make_request(
                url_field_name='adyen_recurring_api_url',
                endpoint='/disable',
                payload=data,
                method='POST'
            )
        except ValidationError:
            pass  # Deactivating the token in Tele is more important than in Adyen

    def _handle_reactivation_request(self):
        """ Override of payment to raise an error informing that Adyen tokens cannot be restored.

        Note: self.ensure_one()

        :return: None
        :raise: UserError if the token is managed by Adyen
        """
        super()._handle_reactivation_request()
        if self.provider != 'adyen':
            return

        raise UserError(_("Saved payment methods cannot be restored once they have been deleted."))
