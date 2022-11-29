# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from unittest import TestCase

from tele.tests import MetaCase


class TestTestSuite(TestCase, metaclass=MetaCase):

    def test_test_suite(self):
        """ Check that TeleSuite handles unittest.TestCase correctly. """
