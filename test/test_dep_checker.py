#!/usr/env python3

import unittest
from dep_checker import dep_checker

class DummyTest(unittest.TestCase):

    def test_a(self):
        self.assertTrue(dep_checker.test_func())
