#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """UnitTest for max_integer function"""

    def test_none(self):
        """Test against an empty list"""

        self.assertIsNone(max_integer([]))

    def test_default(self):
        """Test against a normal case"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_type_error(self):
        """Test against a list that contains a non-number type"""

        self.assertRaises(TypeError, max_integer, [1, 2, 'Hello', 4])

    def test_passing_non_list(self):
        """Test against a non-list type"""

        self.assertRaises(TypeError, max_integer, 4)
