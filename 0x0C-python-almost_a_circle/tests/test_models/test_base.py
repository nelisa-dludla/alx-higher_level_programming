#!/usr/bin/python3
'''
This module contains tests for the base class
'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_with_argument(self):
        base1 = Base(11)
        self.assertEqual(base1.id, 11)

    def test_no_argument(self):
        base1 = Base()
        self.assertEqual(base1.id, 2)

    def test_no_argument_multiple_instances(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        base4 = Base()
        base5 = Base()
        base6 = Base()
        self.assertEqual(base6.id, 8)

    def test_to_json_string_method_with_rectangle(self):
        rect = Rectangle(10, 2, 1, 9, 89)
        rect_dict = rect.to_dictionary()
        rect_json = Base.to_json_string([rect_dict])
        output = '[{"x": 1, "y": 9, "id": 89, "height": 2, "width": 10}]'

        self.assertEqual(rect_json, output)

    def test_to_json_string_method_empty_dict(self):
        rect_json = Base.to_json_string([])
        expected_output = '[]'

        self.assertEqual(rect_json, expected_output)

    def test_to_json_string_method_with_square(self):
        square = Square(10, 2, 1, 89)
        square_dict = square.to_dictionary()
        square_json = Base.to_json_string([square_dict])
        expected_output = '[{"id": 89, "x": 2, "size": 10, "y": 1}]'

        self.assertEqual(square_json, expected_output)

    def test_save_to_file_method(self):
        rect = Rectangle(10, 7, 2, 8, 89)
        Rectangle.save_to_file([rect])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            output = '[{"y": 8, "x": 2, "id": 89, "width": 10, "height": 7}]'
            self.assertEqual(content, output)

    def test_save_to_file_with_none_parsed(self):
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_output = '[]'
            self.assertEqual(content, expected_output)

    def test_from_json_string_method(self):
        json_string = '[{"id": 89, "width": 10, "height": 4}]'
        result = Rectangle.from_json_string(json_string)

        self.assertIsInstance(result, list)

    def test_create_method(self):
        dictionary = {"y": 8, "x": 2, "id": 89, "width": 10, "height": 7}
        result = Rectangle.create(**dictionary)

        self.assertIsInstance(result, Rectangle)
