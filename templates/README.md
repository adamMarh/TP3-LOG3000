# templates/

## Purpose
This directory holds the **Jinja2 HTML templates** rendered by the Flask backend.

## Files
| File | Description |
|------|-------------|
| `index.html` | Main (and only) page of the calculator. Contains the display input, number buttons (0–9), operator buttons (+, −, ×, ÷), a clear button (C) and a submit button (=). JavaScript in a `<script>` block handles appending characters to the display and clearing it. |

## Dependencies
- Flask's `render_template` function (called from `app.py`).
- The CSS file at `static/style.css` (linked via `url_for`).

## Notes
- The form uses `method="POST"` so pressing **=** submits the current display value to the server, which evaluates the expression and returns the result.
- The `display` input is marked `readonly`; user interaction is handled through `onclick` handlers on the buttons.
