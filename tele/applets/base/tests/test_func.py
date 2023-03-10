# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import functools

from tele.tests.common import BaseCase
from tele.tools import frozendict
from tele.tools.func import compose
from tele import Command


class TestCompose(BaseCase):
    def test_basic(self):
        str_add = compose(str, lambda a, b: a + b)
        self.assertEqual(str_add(1, 2), "3")

    def test_decorator(self):
        """ ensure compose() can be partially applied as a decorator
        """
        @functools.partial(compose, str)
        def mul(a, b):
            return a * b

        self.assertEqual(mul(5, 42), u"210")


class TestFrozendict(BaseCase):
    def test_frozendict_immutable(self):
        """ Ensure that a frozendict is immutable. """
        vals = {'name': 'Joe', 'age': 42}
        frozen_vals = frozendict(vals)

        # check __setitem__, __delitem__
        with self.assertRaises(Exception):
            frozen_vals['surname'] = 'Jack'
        with self.assertRaises(Exception):
            frozen_vals['name'] = 'Jack'
        with self.assertRaises(Exception):
            del frozen_vals['name']

        # check update, setdefault, pop, popitem, clear
        with self.assertRaises(Exception):
            frozen_vals.update({'surname': 'Jack'})
        with self.assertRaises(Exception):
            frozen_vals.update({'name': 'Jack'})
        with self.assertRaises(Exception):
            frozen_vals.setdefault('surname', 'Jack')
        with self.assertRaises(Exception):
            frozen_vals.pop('surname', 'Jack')
        with self.assertRaises(Exception):
            frozen_vals.pop('name', 'Jack')
        with self.assertRaises(Exception):
            frozen_vals.popitem()
        with self.assertRaises(Exception):
            frozen_vals.clear()

    def test_frozendict_hash(self):
        """ Ensure that a frozendict is hashable. """
        # dict with simple values
        hash(frozendict({'name': 'Joe', 'age': 42}))

        # dict with tuples, lists, and embedded dicts
        hash(frozendict({
            'user_id': (42, 'Joe'),
            'line_ids': [Command.create({'values': [42]})],
        }))
