#!/usr/bin/python3
"""This is the unittest to determine max integer
"""
import unittest
max_integer = __import__('6-max_integer_0').max_integer


class TestMaxInteger(unittest.TesCase):
    """This class test for max integer
    """
    def testPositive(self):
        self.assertEqual(maxinteger([1, 2, 3, 4]), 4)

    def testNegative(self):
        self.assertEqual(maxinteger([-1, -4, -5, -7]), -1)

    def testMix(self):
        self.asserEqual(max_integer([3, -3, 5, -7, -4]), 5)

    def testWrongInput(self):
        with self.assertRaises(TypeError):
            max_integer("string")

    def testNoneInput(self):
        self.assertIsNone(max_integer[])
