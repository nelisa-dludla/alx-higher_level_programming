#!/usr/bin/python3
'''
Module contains unit tests for Square class
'''
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.square import Square
from models.base import Base


class TestSquare(TestCase):
    def test_no_args_parsed(self):
        with self.assertRaises(TypeError):
            Square()

    def test_size_init_attr_value(self):
        square = Square(2, 3, 4, 5)
        self.assertEqual(square.size, 2)

    def test_x_init_attr_value(self):
        square = Square(2, 3, 4, 5)
        self.assertEqual(square.x, 3)

    def test_y_init_attr_value(self):
        square = Square(2, 3, 4, 5)
        self.assertEqual(square.y, 4)

    def test_id_init_attr_value(self):
        square = Square(2, 3, 4, 5)
        self.assertEqual(square.id, 5)

    def test_size_arg_not_int(self):
        with self.assertRaises(TypeError):
            Square('2', 3, 4, 5)

    def test_x_arg_not_int(self):
        with self.assertRaises(TypeError):
            Square(2, '3', 4, 5)

    def test_y_arg_not_int(self):
        with self.assertRaises(TypeError):
            Square(2, 3, '4', 5)

    def test_size_arg_less_than_zero(self):
        with self.assertRaises(ValueError):
            Square(-2, 3, 4, 5)

    def test_x_arg_less_than_zero(self):
        with self.assertRaises(ValueError):
            Square(2, -3, 4, 5)

    def test_y_arg_less_than_zero(self):
        with self.assertRaises(ValueError):
            Square(2, 3, -4, 5)

    def test_str_method(self):
        square = Square(2, 0, 0, 89)
        str_representation = str(square)
        expected_output = '[Square] (89) 0/0 - 2'

        self.assertEqual(str_representation, expected_output)

    def test_area_no_args_parsed(self):
        with self.assertRaises(TypeError):
            Square().area()

    def test_area_ideal(self):
        square = Square(2)
        self.assertEqual(square.area(), 4)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_method_without_x_y(self, stdout):
        square = Square(2)
        square.display()
        expected_output = '##\n##\n'

        self.assertEqual(stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_method_with_x_y(self, stdout):
        square = Square(2, 1, 1)
        square.display()
        expected_output = '\n ##\n ##\n'

        self.assertEqual(stdout.getvalue(), expected_output)

    def test_display_no_args_parsed(self):
        with self.assertRaises(TypeError):
            Square().display()

    def test_size_getter(self):
        square = Square(2)
        self.assertEqual(square.size, 2)

    def test_size_setter(self):
        square = Square(2)
        square.size = 5
        self.assertEqual(square.size, 5)

    def test_size_attr_not_int(self):
        with self.assertRaises(TypeError):
            Square('2')

    def test_size_attr_less_than_zero(self):
        with self.assertRaises(ValueError):
            Square(-2)

    def test_update_id_attr_with_args(self):
        square = Square(1, 5, 1, 2)
        square.update(89)
        str_representation = str(square)
        expected_output = '[Square] (89) 1/2 - 5'

        self.assertEqual(str_representation, expected_output)

    def test_update_size_attr_with_args(self):
        square = Square(1, 5, 1, 2)
        square.update(89, 10)
        str_representation = str(square)
        expected_output = '[Square] (89) 1/2 - 10'

        self.assertEqual(str_representation, expected_output)

    def test_update_x_attr_with_args(self):
        square = Square(1, 5, 1, 2)
        square.update(89, 10, 3)
        str_representation = str(square)
        expected_output = '[Square] (89) 3/2 - 10'

        self.assertEqual(str_representation, expected_output)

    def test_update_y_attr_with_args(self):
        square = Square(1, 5, 1, 2)
        square.update(89, 10, 3, 4)
        str_representation = str(square)
        expected_output = '[Square] (89) 3/4 - 10'

        self.assertEqual(str_representation, expected_output)

    def test_update_id_attr_with_kwargs(self):
        square = Square(1, 5, 1, 2)
        square.update(id=89)
        str_representation = str(square)
        expected_output = '[Square] (89) 1/2 - 5'

        self.assertEqual(str_representation, expected_output)

    def test_update_size_attr_with_kwargs(self):
        square = Square(89, 5, 1, 2)
        square.update(id=89, size=10)
        str_representation = str(square)
        expected_output = '[Square] (89) 1/2 - 10'

        self.assertEqual(str_representation, expected_output)

    def test_update_x_attr_with_kwargs(self):
        square = Square(89, 5, 1, 2)
        square.update(id=89, x=3)
        str_representation = str(square)
        expected_output = '[Square] (89) 3/2 - 5'

        self.assertEqual(str_representation, expected_output)

    def test_update_y_attr_with_kwargs(self):
        square = Square(89, 5, 1, 2)
        square.update(id=89, y=4)
        str_representation = str(square)
        expected_output = '[Square] (89) 1/4 - 5'

        self.assertEqual(str_representation, expected_output)

    def test_to_dictionary_method(self):
        square = Square(10, 2, 1, 89)
        square_dict = square.to_dictionary()
        expected_output = {'id': 89, 'x': 2, 'size': 10, 'y': 1}

        self.assertEqual(square_dict, expected_output)
