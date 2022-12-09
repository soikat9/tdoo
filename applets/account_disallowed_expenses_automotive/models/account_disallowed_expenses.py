# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class AccountDisallowedExpensesCategory(models.Model):
    _inherit = 'account.disallowed.expenses.category'

    car_category = fields.Boolean('Car Category', help='This checkbox makes the vehicle mandatory while booking a vendor bill.')

    def name_get(self):
        res = super().name_get()
        # Do no display the rate in the name for car expenses
        for i in range(len(res)):
            category = self.browse(res[i][0])
            if category.car_category:
                res[i] = (res[i][0], '%s - %s' % (category.code, category.name))
        return res
