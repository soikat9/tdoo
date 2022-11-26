# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


class ConverterTest(models.Model):
    _name = 'web_editor.converter.test'
    _description = 'Web Editor Converter Test'

    # disable translation export for those brilliant field labels and values
    _translate = False

    char = fields.Char()
    integer = fields.Integer()
    float = fields.Float()
    numeric = fields.Float(digits=(16, 2))
    many2one = fields.Many2one('web_editor.converter.test.sub')
    binary = fields.Binary(attachment=False)
    date = fields.Date()
    datetime = fields.Datetime()
    selection_str = fields.Selection([
        ('A', "Test1"),
        ('B', "Test2"),
        ('C', "Test3"),
        ('D', "Test4"),
    ], string=u"Test"
              fu"qu'il fait une escale technique à St Claude, on dit:")
    html = fields.Html()
    text = fields.Text()


class ConverterTestSub(models.Model):
    _name = 'web_editor.converter.test.sub'
    _description = 'Web Editor Converter Subtest'

    name = fields.Char()
