# -*- coding: utf-8 -*-

from tele import models, fields, api


class onboarding_banner(models.Model):
    _name = 'onboarding_banner.onboarding_banner'
    _description = 'onboarding_banner.onboarding_banner'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
