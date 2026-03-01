"""app.py — Main Flask application for the web calculator.

This module defines the Flask web server, the expression parsing logic,
and the single route that serves the calculator UI and handles form
submissions.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Create the Flask application instance
app = Flask(__name__)

# Map operator characters to their corresponding arithmetic functions
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """Parse and evaluate a simple arithmetic expression.

    The expression must contain exactly two numeric operands separated by
    a single operator (+, -, *, /).  Spaces are stripped before parsing.

    Args:
        expr: A string such as ``"3+5"`` or ``"12 / 4"``.

    Returns:
        The numeric result of the operation (float).

    Raises:
        ValueError: If the expression is empty, contains more than one
            operator, has an operator at an invalid position, or has
            non-numeric operands.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Remove all spaces so that "3 + 5" becomes "3+5"
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Walk through the string to locate the operator
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Operator must not be the first or last character
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    # Split expression into left and right operands
    left = s[:op_pos]
    right = s[op_pos+1:]

    # Convert operand strings to floats
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Dispatch the operation using the OPS mapping
    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Serve the calculator page and process form submissions.

    On GET, renders the calculator with an empty display.
    On POST, evaluates the expression sent from the form and
    renders the result (or an error message) on the display.

    Returns:
        Rendered HTML of the calculator page.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)