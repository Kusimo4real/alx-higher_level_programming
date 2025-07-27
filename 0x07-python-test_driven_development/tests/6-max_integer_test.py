#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 2, 4, 3, 0]), 4)
    def test_max_only(self):
        self.assertEqual(max_integer([4]), 4)
    def test_max_at_begining(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    def test_negative_number(self):
        self.assertEqual(max_integer([4, -2, 1, 3]), 4)
    def test_contain_negative_number(self):
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

if __name__ == '__main__':
    unittest.main()
