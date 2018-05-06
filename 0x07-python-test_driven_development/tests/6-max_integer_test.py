#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """test for numbers"""
    def testerrors(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 1, 0, -1]), 5)
        self.assertEqual(max_integer([9, 9, 9]), 9)

    """test for empty list"""
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, None)
    """test for strings"""
    def test_if_string_passed(self):
        self.assertRaises(TypeError, max_integer, [7, 1, 8, "Darnell"])
        self.assertRaises(TypeError, max_integer, ["G", 4, 1, 5])
        self.assertRaises(TypeError, max_integer, [2, 1, "Dog", 4,  2])
