# static/

## Purpose
This directory contains all **static assets** (CSS, images, JavaScript) served by Flask's built-in static file handler.

## Files
| File | Description |
|------|-------------|
| `style.css` | Provides the full visual styling for the calculator page: centered layout, dark-themed calculator body, grid-based button layout, and hover/active states for buttons. |

## Dependencies
- Referenced from `templates/index.html` via `{{ url_for('static', filename='style.css') }}`.

## Notes
- The calculator layout uses CSS Grid (`grid-template-columns: repeat(4, 1fr)`) to arrange buttons in a 4-column grid.
- Operator buttons are styled with a distinct orange background (`.operator` class).
