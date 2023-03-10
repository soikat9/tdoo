# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    subscription_count = fields.Integer(string='Subscriptions', compute='_subscription_count')

    def write(self, vals):
        if 'active' in vals and not vals.get('active'):
            Subscription = self.env['sale.subscription']
            Subscription.sudo().search([('partner_invoice_id', 'in', self.ids)]).partner_invoice_id = False
            Subscription.sudo().search([('partner_shipping_id', 'in', self.ids)]).partner_shipping_id = False
        return super().write(vals)

    def _subscription_count(self):
        # retrieve all children partners and prefetch 'parent_id' on them
        all_partners = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        all_partners.read(['parent_id'])

        subscription_data = self.env['sale.subscription'].read_group(
            domain=[('partner_id', 'in', all_partners.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )

        self.subscription_count = 0
        for group in subscription_data:
            partner = self.browse(group['partner_id'][0])
            while partner:
                if partner in self:
                    partner.subscription_count += group['partner_id_count']
                partner = partner.parent_id
