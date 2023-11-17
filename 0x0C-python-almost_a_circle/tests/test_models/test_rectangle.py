#!/usr/bin/python3
'''
Module contains unit tests for Rectangle class
'''
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(TestCase):
    def test_no_args_parsed(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg_parsed(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_width_init_attr_value(self):
        square1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(square1.width, 10)

    def test_height_init_attr_value(self):
        square1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(square1.height, 2)

    def test_x_init_attr_value(self):
        square1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(square1.x, 0)

    def test_y_init_attr_value(self):
        square1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(square1.y, 0)

    def test_id_init_attr_value(self):
        square1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(square1.id, 12)

    def test_id_init_attr_without_id_parsed(self):
        square1 = Rectangle(10, 2, 0, 0)
        self.assertEqual(square1.id, 12)

    def test_width_arg_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle('10', 2, 0, 0)

    def test_height_arg_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(10, '2', 0, 0)

    def test_x_arg_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, '0', 0)

    def test_y_arg_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, '0')

    def test_width_arg_less_than_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 2, 0, 0)

    def test_height_arg_less_than_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -2, 0, 0)

    def test_x_arg_less_than_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 0)

    def test_y_arg_less_than(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area_no_args_parsed(self):
        with self.assertRaises(TypeError):
            Rectangle().area()

    def test_area_one_arg_parsed(self):
        with self.assertRaises(TypeError):
            Rectangle(8).area()

    def test_area_two_args_parsed(self):
        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_method_without_x_y(self, stdout):
        rect = Rectangle(2, 2)
        rect.display()
        expected_output = '##\n##\n'

        self.assertMultiLineEqual(stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_method_with_x_y(self, stdout):
        rect = Rectangle(2, 3, 2, 2)
        rect.display()
        expected_output = '\n\n  ##\n  ##\n  ##\n'

        self.assertMultiLineEqual(stdout.getvalue(), expected_output)

    def test_str_method_all_attr_parsed(self):
        rect = Rectangle(4, 6, 2, 1, 12)
        str_representation = str(rect)
        expected_output1 = '[Rectangle] (12) 2/1 - 4/6'

        self.assertEqual(str_representation, expected_output1)

    def test_str_method_some_args_missing(self):
        rect = Rectangle(5, 5, 1)
        str_representation = str(rect)
        expected_output = '[Rectangle] (13) 1/0 - 5/5'

        self.assertEqual(str_representation, expected_output)

    def test_update_id_attr_with_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89)
        str_representation = str(rect)
        expected_output = '[Rectangle] (89) 10/10 - 10/10'

        self.assertEqual(str_representation, expected_output)

    def test_update_width_attr_with_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2)
        str_representation = str(rect)
        expected_output = '[Rectangle] (89) 10/10 - 2/10'

        self.assertEqual(str_representation, expected_output)

    def test_update_height_attr_with_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3)
        str_representation = str(rect)
        expected_output = '[Rectangle] (89) 10/10 - 2/3'

        self.assertEqual(str_representation, expected_output)

    def test_update_x_attr_with_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3, 4)
        str_representation = str(rect)
        expected_output = '[Rectangle] (89) 4/10 - 2/3'

        self.assertEqual(str_representation, expected_output)

    def test_update_y_attr_with_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5)
        str_representation = str(rect)
        expected_output = '[Rectangle] (89) 4/5 - 2/3'

        self.assertEqual(str_representation, expected_output)

    def test_update_id_attr_with_kwargs(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=89)
        str_representation = str(rect)
        expected_output = '[Rectangle] (89) 10/10 - 10/10'

        self.assertEqual(str_representation, expected_output)

    def test_update_width_attr_with_kwargs(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=89, width=2)
        str_representation = str(rect)
        expected_output = '[Rectangle] (89) 10/10 - 2/10'

        self.assertEqual(str_representation, expected_output)

    def test_update_height_attr_with_kwargs(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=89, height=3)
        str_representation = str(rect)
        expected_output = '[Rectangle] (89) 10/10 - 10/3'

        self.assertEqual(str_representation, expected_output)

    def test_update_x_attr_with_kwargs(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=89, x=4)
        str_representation = str(rect)
        expected_output = '[Rectangle] (89) 4/10 - 10/10'

        self.assertEqual(str_representation, expected_output)

    def test_update_y_attr_with_kwargs(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=89, y=5)
        str_representation = str(rect)
        expected_output = '[Rectangle] (89) 10/5 - 10/10'

        self.assertEqual(str_representation, expected_output)

    def test_to_dictionary_method(self):
        rect = Rectangle(10, 2, 1, 9, 89)
        rect_dict = rect.to_dictionary()
        output = {'x': 1, 'y': 9, 'id': 89, 'height': 2, 'width': 10}

        self.assertEqual(rect_dict, output)
