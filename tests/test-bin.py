# -*- coding: utf-8 -*-

from .context import ooex

import unittest

class TestBin(unittest.TestCase):
    """Unit tests for the Bin class"""

    def setUp(self):
        self.five = ooex.Outcome("00-0-1-2-3", 6)
        self.zero = ooex.Bin(ooex.Outcome("0", 35))

    def test_add(self):
        self.zero = self.zero.add(self.five)
        self.assertEqual(len(self.zero), 2)


if __name__ == '__main__':
    unittest.main()
