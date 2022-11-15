# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.tests import BaseCase
from tele.tools.rendering_tools import parse_inline_template

class TestParseInlineTemplate(BaseCase):
    def test_no_expression(self):
        text = 'a b c'
        self.assertEqual(parse_inline_template(text), [('a b c', '')])

    def test_expression1(self):
        text = 'a {{b}}'
        self.assertEqual(parse_inline_template(text), [('a ', 'b')])

    def test_expression2(self):
        text = 'a {{b}} c'
        self.assertEqual(parse_inline_template(text), [('a ', 'b'), (' c', '')])
