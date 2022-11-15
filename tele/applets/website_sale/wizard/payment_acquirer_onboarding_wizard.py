# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class PaymentWizard(models.TransientModel):
    _inherit = 'payment.acquirer.onboarding.wizard'
    _name = 'website.sale.payment.acquirer.onboarding.wizard'
    _description = 'Website Payment acquire onboarding wizard'

    def _set_payment_acquirer_onboarding_step_done(self):
        """ Override. """
        self.env.company.sudo().set_onboarding_step_done('payment_acquirer_onboarding_state')

    def _start_stripe_onboarding(self):
        """ Override of payment to set the dashboard as start menu of the payment onboarding. """
        menu_id = self.env.ref('website.menu_website_dashboard').id
        return self.env.company._run_payment_onboarding_step(menu_id)
