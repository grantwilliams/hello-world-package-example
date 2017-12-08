#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_hello_world
----------------------------------

Tests for `hello_world` module.
"""

import unittest

import hello_world


class TestHello_world(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(hello_world.__version__)

    def tearDown(self):
        pass
