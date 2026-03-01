# tests/

## Purpose
This directory contains the **automated test suite** for the Flask Calculator project. Tests are written with Python's built-in `unittest` framework and can also be executed via `pytest`.

## Files
| File | Description |
|------|-------------|
| `test_operators.py` | Unit tests for every function in `operators.py` (add, subtract, multiply, divide). These tests expose the three known bugs. |
| `test_app.py` | Integration tests for the Flask application: verifies the `calculate()` function and the HTTP route. |

## How to Run

```bash
# From the project root directory
python -m pytest tests/ -v
```

Or with unittest:
```bash
python -m unittest discover -s tests -v
```

## What the Tests Cover
- **Addition**: verifies `add(a, b)` returns the correct sum.
- **Subtraction**: verifies `subtract(a, b)` returns `a - b` (currently fails due to operand swap bug).
- **Multiplication**: verifies `multiply(a, b)` returns `a * b` (currently fails because `**` is used instead of `*`).
- **Division**: verifies `divide(a, b)` returns true division `a / b` (currently fails because `//` floor division is used).
- **Expression parsing**: verifies `calculate()` correctly parses and evaluates simple expressions.
- **Edge cases**: empty input, invalid operators, division by zero, non-numeric operands.
