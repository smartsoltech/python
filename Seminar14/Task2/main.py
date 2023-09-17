import doctest
import unittest
import pytest

class InvalidMatrixOperation(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        return self.add_matrices(other)

    def __mul__(self, other):
        return self.multiply_matrices(other)

    def add_matrices(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise InvalidMatrixOperation("Matrices must have the same dimensions for addition.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def multiply_matrices(self, other):
        if self.cols != other.rows:
            raise InvalidMatrixOperation("Number of columns of the first matrix must be equal to the number of rows of the second matrix.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                cell = 0
                for k in range(self.cols):
                    cell += self.data[i][k] * other.data[k][j]
                row.append(cell)
            result.append(row)
        return Matrix(result)

# Doctest
"""
>>> m1 = Matrix([[1, 2], [3, 4]])
>>> m2 = Matrix([[5, 6], [7, 8]])
>>> (m1 + m2).data
[[6, 8], [10, 12]]

>>> m3 = Matrix([[1, 2], [3, 4]])
>>> m4 = Matrix([[5, 6], [7, 8]])
>>> (m3 * m4).data
[[19, 22], [43, 50]]
"""

doctest.testmod()

# Unittest

class TestMatrixOperations(unittest.TestCase):
    def test_addition(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        self.assertEqual((m1 + m2).data, [[6, 8], [10, 12]])

    def test_multiplication(self):
        m3 = Matrix([[1, 2], [3, 4]])
        m4 = Matrix([[5, 6], [7, 8]])
        self.assertEqual((m3 * m4).data, [[19, 22], [43, 50]])

if __name__ == '__main__':
    unittest.main()

# Pytest

def test_addition_pytest():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    assert (m1 + m2).data == [[6, 8], [10, 12]]

def test_multiplication_pytest():
    m3 = Matrix([[1, 2], [3, 4]])
    m4 = Matrix([[5, 6], [7, 8]])
    assert (m3 * m4).data == [[19, 22], [43, 50]]
