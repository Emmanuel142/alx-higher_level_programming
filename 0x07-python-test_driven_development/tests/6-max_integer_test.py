#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TesCase):
    """This class test for max integer
    """
    def test_max():
        self.assertEqual(maxinteger([1, 2, 3, 4]), 4)
