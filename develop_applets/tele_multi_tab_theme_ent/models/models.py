# -*- coding: utf-8 -*-

from tele import models, fields, api


class tele_multi_tab_theme_ent(models.Model):
    _name = 'tele_multi_tab_theme_ent.tele_multi_tab_theme_ent'
    _description = 'tele_multi_tab_theme_ent.tele_multi_tab_theme_ent'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
