#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def testPositiveValues(self):
        '''Test list with positive values'''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def testNegativeValues(self):
        '''Test list of negative values'''
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def testEmptyList(self):
        '''Test if list is empty'''
        self.assertEqual(max_integer([]), None)

    def testNoArgumentParsed(self):
        '''Test if no argument is entered'''
        self.assertEqual(max_integer(), None)

    def testMixedValues(self):
        '''Test if list contains mixed values'''
        self.assertRaises(TypeError, max_integer, ['Alx', 2, True])
