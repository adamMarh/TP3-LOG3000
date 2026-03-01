"""test_operators.py — Unit tests for the arithmetic operator functions.

Each test case targets one function from operators.py and asserts its
expected behaviour.  Three of these tests are designed to **fail** against
the original (buggy) code, confirming the bugs reported in the GitHub
issues.
"""

import unittest
import sys
import os

# Ensure the project root is on the Python path so we can import operators
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from operators import add, subtract, multiply, divide


class TestAdd(unittest.TestCase):
    """Tests for the add() function."""

    def test_add_positive_numbers(self):
        """add(2, 3) should return 5."""
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        """add(-1, -1) should return -2."""
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        """add(0, 5) should return 5."""
        self.assertEqual(add(0, 5), 5)


class TestSubtract(unittest.TestCase):
    """Tests for the subtract() function.

    BUG: subtract currently computes b - a instead of a - b.
    The following test will FAIL on the buggy code.
    """

    def test_subtract_basic(self):
        """subtract(10, 3) should return 7, not -7."""
        self.assertEqual(subtract(10, 3), 7)

    def test_subtract_negative_result(self):
        """subtract(3, 10) should return -7."""
        self.assertEqual(subtract(3, 10), -7)


class TestMultiply(unittest.TestCase):
    """Tests for the multiply() function.

    BUG: multiply currently computes a ** b (exponentiation) instead of a * b.
    The following test will FAIL on the buggy code.
    """

    def test_multiply_basic(self):
        """multiply(4, 5) should return 20, not 1024."""
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_by_zero(self):
        """multiply(7, 0) should return 0."""
        self.assertEqual(multiply(7, 0), 0)


class TestDivide(unittest.TestCase):
    """Tests for the divide() function.

    BUG: divide currently uses floor division (//) instead of true division (/).
    The following test will FAIL on the buggy code.
    """

    def test_divide_exact(self):
        """divide(10, 2) should return 5.0."""
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_non_integer_result(self):
        """divide(7, 2) should return 3.5, not 3."""
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """divide(5, 0) should raise ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


if __name__ == '__main__':
    unittest.main()
