# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields

class test_uninstall_model(models.Model):
    """
    This model uses different types of columns to make it possible to test
    the uninstall feature of Tele.
    """
    _name = 'test_uninstall.model'
    _description = 'Testing Uninstall Model'

    name = fields.Char('Name')
    ref = fields.Many2one('res.users', string='User')
    rel = fields.Many2many('res.users', string='Users')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Each name must be unique.'),
    ]
