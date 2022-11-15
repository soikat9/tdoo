# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class IrExports(models.Model):
    _name = "ir.exports"
    _description = 'Exports'
    _order = 'name'

    name = fields.Char(string='Export Name')
    resource = fields.Char(index=True)
    export_fields = fields.One2many('ir.exports.line', 'export_id', string='Export ID', copy=True)


class IrExportsLine(models.Model):
    _name = 'ir.exports.line'
    _description = 'Exports Line'
    _order = 'id'

    name = fields.Char(string='Field Name')
    export_id = fields.Many2one('ir.exports', string='Export', index=True, ondelete='cascade')