#!/usr/bin/python3
"""Define unittests for the Rectangle model
unittest class:
    TestRectangle_instantiation
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_y
"""

import os
import sys
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of Rectangle 
    class
    """
    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(10, 2, 3)
        r2 = Rectangle(2, 10, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(10, 2, 3, 4)
        r2 = Rectangle(2, 10, 4, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(11, Rectangle(7, 8, 9, 10, 11).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    """Unittest testcases of private attributes"""

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    """Unittest testcases for Getters and Setters"""

    def test_getter_width(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_setter_width(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_getter_height(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_setter_height(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 11
        self.assertEqual(11, r.height)

    def test_getter_x(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_setter_x(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 12
        self.assertEqual(12, r.x)

    def test_getter_y(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_setter_y(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 13
        self.assertEqual(13, r.y)

    """Unittest testcases for area method"""

    def test_area(self):
        r = Rectangle(3, 5, 0, 0, 1)
        self.assertEqual(15, r.area())

if __name__ == "__main__":
    unittest.main()
