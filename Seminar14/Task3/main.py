import doctest
import unittest
import pytest


class InvalidRectangleSide(Exception):
    def __init__(self, side):
        self.message = f"Invalid length of side: {side}. Side length should be positive."
        super().__init__(self.message)

class Rectangle:
    def __init__(self, length, width):
        self.validate_sides(length, width)
        self.length = length
        self.width = width

    def validate_sides(self, length, width):
        if length <= 0 or width <= 0:
            raise InvalidRectangleSide(min(length, width))

# Doctest
"""
>>> r = Rectangle(5, 10)
>>> r.length
5
>>> r.width
10

>>> Rectangle(-1, 10)
Traceback (most recent call last):
    ...
InvalidRectangleSide: Invalid length of side: -1. Side length should be positive.
"""

doctest.testmod()

# Unittest

class TestRectangle(unittest.TestCase):
    def test_valid_rectangle(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.length, 5)
        self.assertEqual(r.width, 10)

    def test_invalid_rectangle(self):
        with self.assertRaises(InvalidRectangleSide):
            Rectangle(-1, 10)

if __name__ == '__main__':
    unittest.main()

# Pytest

def test_valid_rectangle_pytest():
    r = Rectangle(5, 10)
    assert r.length == 5
    assert r.width == 10

def test_invalid_rectangle_pytest():
    with pytest.raises(InvalidRectangleSide):
        Rectangle(-1, 10)
