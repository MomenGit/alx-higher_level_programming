#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """UnitTest for max_integer function"""

    def test_module_docstring(self):
        """Tests for module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """Test against an empty list"""
        self.assertIsNone(max_integer([]))

    def test_default(self):
        """Test against a normal case"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        on = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(on), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def test_type_error(self):
        """Test against a list that contains a non-number type"""
        self.assertRaises(TypeError, max_integer, [1, 2, 'Hello', 4])

    def test_passing_non_list(self):
        """Test against a non-list type"""
        self.assertRaises(TypeError, max_integer, 4)


if __name__ == "__main__":
    unittest.main()
