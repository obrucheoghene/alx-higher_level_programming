#!/usr/bin/python3
"""
This module discribes a unittest for the max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This are testCase for the max_integer function.
    """

    def test_regular(self):
        """
        Test with a regular list of ints: should return the max result
        """
        list = [1, 2, 3, 4, 5]
        result = max_integer(list)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """
        Test with a list of non-ints and ints:
        """
        list = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, list)

    def test_empty(self):
        """
        Test with an empty list
        """
        list = []
        result = max_integer(list)
        self.assertEqual(result, None)

    def test_negative(self):
        """
        Test with a list of negative values
        """
        list = [-2, -6, -1]
        result = max_integer(list)
        self.assertEqual(result, -1)

    def test_float(self):
        """
        Test with a list of mixed ints and floats
        """
        list = [3, 4.5, 2]
        result = max_integer(list)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """
        Test with a argument that's not a list
        """
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """
        Test with a list of one int
        """
        list = [45]
        result = max_integer(list)
        self.assertEqual(result, 45)

    def test_identical(self):
        """
        Test with a list of identical values
        """
        list = [8, 8, 8, 8, 8]
        result = max_integer(list)
        self.assertEqual(result, 8)

    def test_strings(self):
        """
        Test with a list of strings
        """
        list = ["hi", "hello"]
        result = max_integer(list)
        self.assertEqual(result, "hi")

    def test_none(self):
        """
        Test with a None as argument
        """
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
