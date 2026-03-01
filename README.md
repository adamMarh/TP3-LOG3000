# Flask Calculator

## Project Name
**Flask Calculator** – A simple web-based arithmetic calculator.

## Team
Équipe X – LOG3000

## Objective
Provide a minimal, browser-based calculator that supports the four basic arithmetic operations (addition, subtraction, multiplication, division) using a Python/Flask backend and a vanilla HTML/CSS/JS frontend.

---

## Prerequisites
| Tool | Minimum version |
|------|-----------------|
| Python | 3.9+ |
| pip | 21+ |
| Git | 2.30+ |
| A modern web browser | — |

## Installation

```bash
# 1. Clone the repository
git clone <REPO_URL>
cd TP3---LOG3000

# 2. (Optional) Create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install flask

# 4. Run the application
python app.py
```

The server starts at **http://127.0.0.1:5000**.

## Usage
1. Open your browser and go to `http://127.0.0.1:5000`.
2. Click the number and operator buttons to build an expression (e.g. `12+8`).
3. Press **=** to submit the expression. The result (or an error message) is shown in the display.
4. Press **C** to clear the display.

## Running Tests

```bash
# From the project root
python -m pytest tests/ -v
```

All tests are located in the `tests/` directory. See `tests/README.md` for details on what is covered.

## Contribution Workflow
1. Create a new branch from `main` for each issue or feature:
   ```bash
   git checkout -b fix/issue-<number>
   ```
2. Make your changes and commit with a clear message explaining *what* was changed and *why*.
3. Push the branch and open a **Pull Request** (PR) on GitHub.
4. At least one team member must review the PR before merging.
5. After approval, merge the PR into `main` and delete the feature branch.

## Project Structure
```
TP3---LOG3000/
├── app.py            # Flask server & expression parser
├── operators.py      # Arithmetic operator functions
├── static/
│   └── style.css     # Calculator styling
├── templates/
│   └── index.html    # Calculator HTML page
├── tests/
│   ├── test_operators.py   # Unit tests for operators
│   ├── test_app.py         # Integration tests for the app
│   └── README.md           # Test documentation
└── README.md         # This file
```

## License
This repository is part of a university assignment (LOG3000) and is not licensed for external use.
