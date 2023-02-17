#!/usr/bin/python3
"""Defines unittests for base class and methods
unittest classes:
    TestBase_instantiation
    """
import os
import unittest

from models.base import Base

class TestBase_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of a base class"""

    def test_no_arg(self):
        """Basically if id has no given argument
        for objects, then the 2nd objects id should be
        1 > than the base of the 1st objects id"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """If no arguments are given to 3 seperate base 
        objects, the id of all objects should increment 
        respectively by 1."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_is_int(self):
        with self.assertRaises(TypeError):
            Base.id != type(int)

if __name__ == "__main__":
    unittest.main()
