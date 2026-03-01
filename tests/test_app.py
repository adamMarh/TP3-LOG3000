"""test_app.py — Integration tests for the Flask calculator application.

These tests verify the expression-parsing logic in ``calculate()`` and the
HTTP behaviour of the ``/`` route.
"""

import unittest
import sys
import os

# Ensure the project root is on the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, calculate


class TestCalculateFunction(unittest.TestCase):
    """Tests for the calculate() helper function."""

    def test_addition_expression(self):
        """calculate('2+3') should return 5.0."""
        self.assertEqual(calculate('2+3'), 5.0)

    def test_expression_with_spaces(self):
        """Spaces in the expression should be ignored."""
        self.assertEqual(calculate('2 + 3'), 5.0)

    def test_empty_expression_raises(self):
        """An empty string should raise ValueError."""
        with self.assertRaises(ValueError):
            calculate('')

    def test_no_operator_raises(self):
        """An expression without an operator should raise ValueError."""
        with self.assertRaises(ValueError):
            calculate('42')

    def test_multiple_operators_raises(self):
        """An expression with more than one operator should raise ValueError."""
        with self.assertRaises(ValueError):
            calculate('1+2+3')

    def test_non_numeric_operand_raises(self):
        """Non-numeric operands should raise ValueError."""
        with self.assertRaises(ValueError):
            calculate('abc+2')


class TestFlaskRoute(unittest.TestCase):
    """Tests for the HTTP route '/'."""

    def setUp(self):
        """Create a test client for the Flask app."""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_get_returns_200(self):
        """GET / should return HTTP 200."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_with_valid_expression(self):
        """POST with a valid expression should return 200 and show a result."""
        response = self.client.post('/', data={'display': '2+3'})
        self.assertEqual(response.status_code, 200)

    def test_post_with_invalid_expression(self):
        """POST with an invalid expression should still return 200 (error shown in page)."""
        response = self.client.post('/', data={'display': ''})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
