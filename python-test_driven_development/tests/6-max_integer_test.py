#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 5, 2, 1]), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -2, -30]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 5, -2]), 5)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_equal(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 999999, 5000000, 123456]), 5000000)


if __name__ == '__main__':
    unittest.main()
