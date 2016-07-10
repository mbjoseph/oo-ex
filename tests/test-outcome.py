# -*- coding: utf-8 -*-

from .context import ooex

import unittest

class TestOutcome(unittest.TestCase):
    def setUp(self):
        """Set up tests for the Outcome class

        Creates three tests that vary in their attributes.
        """
        self.Outcome1 = ooex.Outcome('Red', 3)
        self.Outcome2 = ooex.Outcome('Red', 5)
        self.Outcome3 = ooex.Outcome('Black', 3)

    def test_equality(self):
        """Test for equality method"""
        self.assertEqual(self.Outcome1, self.Outcome2)

    def test_non_equality(self):
        """Test inequality method"""
        self.assertNotEqual(self.Outcome1, self.Outcome3)

    def test_win_amount(self):
        """Test that winAmount multiplies correctly"""
        self.assertEqual(self.Outcome3.winAmount(5), 15)
        self.assertEqual(self.Outcome2.winAmount(0.5), 2.5)

if __name__ == '__main__':
    unittest.main()
