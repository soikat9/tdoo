# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"
    _mailing_enabled = True

    def _mailing_get_default_domain(self, mailing):
        return [('stage_category', '=', 'progress')]

    def _sms_get_number_fields(self):
        """ No phone or mobile field is available on subscription model. Instead
        SMS will fallback on partner-based computation using ``_sms_get_partner_fields``. """
        return []

    def _sms_get_partner_fields(self):
        return ['partner_id']
