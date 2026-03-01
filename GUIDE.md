# ============================================================
#        GUIDE – Remaining Manual Steps for TP3 (LOG3000)
# ============================================================
# This document describes every action you must perform on
# GitHub (and locally via git) to complete the lab deliverables.
# Follow the steps IN ORDER.
# ============================================================


# ===================== PHASE 0 – LOCAL PREP ==================
#
# All code changes have ALREADY been made locally:
#   • Docstrings & comments added to every file
#   • README.md created at project root, templates/, static/, tests/
#   • Test suite created in tests/ (test_operators.py, test_app.py)
#   • 3 bugs FIXED in operators.py (subtract, multiply, divide)
#   • HTML display bugs fixed in index.html
#   • All 19 tests pass (run: python -m pytest tests/ -v)
#
# IMPORTANT: Before proceeding you need to UNDO the 3 bug fixes
# in operators.py so that the buggy version is committed to main
# first.  The fixes will be applied on separate branches.
#
# To revert operators.py to the buggy state, run:
#
#   cd TP3---LOG3000
#   git checkout -- operators.py
#
# Then re-apply ONLY the docstrings (without fixing the bugs).
# The easiest approach: edit operators.py manually so the
# function bodies are buggy again but the docstrings remain.
# Specifically, make the 3 functions look like this:
#
#   def subtract(a, b):
#       """...(keep docstring)..."""
#       return b - a
#
#   def multiply(a, b):
#       """...(keep docstring)..."""
#       return a ** b
#
#   def divide(a, b):
#       """...(keep docstring)..."""
#       return a // b
#
# I have prepared a clean "buggy-but-documented" version of
# operators.py below (Section APPENDIX-A) that you can paste.


# ============= PHASE 1 – CREATE GITHUB REPO (10 pts) =========
#
# 1. Go to https://github.com/new
# 2. Repository name: TP3---LOG3000  (or any name you prefer)
# 3. Description: "Simple Flask web calculator – LOG3000 TP3"
# 4. Visibility: Private (make Public before deadline)
# 5. Do NOT initialize with a README (we already have one)
# 6. Click "Create repository"
#
# 7. Add collaborators:
#    Settings → Collaborators → Add people → enter each team
#    member's GitHub username → Send invitation
#
# 8. Push the local repo (with buggy operators.py + docs + tests):
#
#    cd TP3---LOG3000
#    git remote set-url origin https://github.com/<YOU>/TP3---LOG3000.git
#      (or git remote add origin ... if no remote exists)
#    git add -A
#    git commit -m "Initial commit: add documentation, README files, and test suite"
#    git push -u origin main
#
# 9. Verify on GitHub that README.md is displayed on the repo page
#    and all files are present.


# ============= PHASE 2 – RUN TESTS & OPEN ISSUES (20 pts) ====
#
# Run the tests (they should show 5 failures on the buggy code):
#
#    python -m pytest tests/ -v
#
# Expected failures:
#   FAILED test_subtract_basic           → subtract returns b-a instead of a-b
#   FAILED test_subtract_negative_result → same root cause
#   FAILED test_multiply_basic           → multiply uses ** instead of *
#   FAILED test_multiply_by_zero         → same root cause
#   FAILED test_divide_non_integer_result→ divide uses // instead of /
#
# Open 3 GitHub Issues (one per bug):
#
# ── Issue #1 ──────────────────────────────────────────────
# Title:   Bug: subtract() returns b - a instead of a - b
# Body:
#   ## Description
#   The `subtract` function in `operators.py` computes `b - a`
#   instead of `a - b`, reversing the operand order.
#
#   ## Steps to reproduce
#   ```python
#   from operators import subtract
#   result = subtract(10, 3)
#   print(result)  # prints -7, expected 7
#   ```
#
#   ## Failing tests
#   - `test_subtract_basic`
#   - `test_subtract_negative_result`
#
#   ## Expected behaviour
#   `subtract(10, 3)` should return `7`.
# Labels: bug
# Assignee: <team member 1>
#
# ── Issue #2 ──────────────────────────────────────────────
# Title:   Bug: multiply() uses exponentiation instead of multiplication
# Body:
#   ## Description
#   The `multiply` function in `operators.py` uses the `**`
#   operator (exponentiation) instead of `*` (multiplication).
#
#   ## Steps to reproduce
#   ```python
#   from operators import multiply
#   result = multiply(4, 5)
#   print(result)  # prints 1024, expected 20
#   ```
#
#   ## Failing tests
#   - `test_multiply_basic`
#   - `test_multiply_by_zero`
#
#   ## Expected behaviour
#   `multiply(4, 5)` should return `20`.
# Labels: bug
# Assignee: <team member 2>
#
# ── Issue #3 ──────────────────────────────────────────────
# Title:   Bug: divide() uses floor division instead of true division
# Body:
#   ## Description
#   The `divide` function in `operators.py` uses `//` (floor
#   division) instead of `/` (true division), truncating decimal
#   results.
#
#   ## Steps to reproduce
#   ```python
#   from operators import divide
#   result = divide(7, 2)
#   print(result)  # prints 3, expected 3.5
#   ```
#
#   ## Failing tests
#   - `test_divide_non_integer_result`
#
#   ## Expected behaviour
#   `divide(7, 2)` should return `3.5`.
# Labels: bug
# Assignee: <team member 3 (or yourself)>


# ======== PHASE 3 – FIX BUGS ON BRANCHES (20 pts) ============
#
# For EACH issue, create a branch, fix the bug, verify, commit.
#
# ── Fix subtract (Issue #1) ──────────────────────────────
#
#    git checkout main
#    git checkout -b fix/issue-1-subtract
#
#    Edit operators.py line:
#      OLD:  return b - a
#      NEW:  return a - b
#
#    Run tests:  python -m pytest tests/test_operators.py::TestSubtract -v
#    (both subtract tests should now PASS)
#
#    git add operators.py
#    git commit -m "fix(subtract): swap operands to compute a - b instead of b - a
#
#    The subtract function incorrectly returned b - a, reversing
#    the expected result.  Changed to a - b.
#
#    Closes #1"
#    git push -u origin fix/issue-1-subtract
#
# ── Fix multiply (Issue #2) ──────────────────────────────
#
#    git checkout main
#    git checkout -b fix/issue-2-multiply
#
#    Edit operators.py line:
#      OLD:  return a ** b
#      NEW:  return a * b
#
#    Run tests:  python -m pytest tests/test_operators.py::TestMultiply -v
#    (both multiply tests should now PASS)
#
#    git add operators.py
#    git commit -m "fix(multiply): use multiplication (*) instead of exponentiation (**)
#
#    The multiply function used the ** operator, performing
#    exponentiation instead of multiplication.  Changed to *.
#
#    Closes #2"
#    git push -u origin fix/issue-2-multiply
#
# ── Fix divide (Issue #3) ────────────────────────────────
#
#    git checkout main
#    git checkout -b fix/issue-3-divide
#
#    Edit operators.py line:
#      OLD:  return a // b
#      NEW:  return a / b
#
#    Run tests:  python -m pytest tests/test_operators.py::TestDivide -v
#    (all divide tests should now PASS)
#
#    git add operators.py
#    git commit -m "fix(divide): use true division (/) instead of floor division (//)
#
#    The divide function used floor division (//), truncating
#    decimal results.  Changed to true division (/).
#
#    Closes #3"
#    git push -u origin fix/issue-3-divide


# ======= PHASE 4 – PULL REQUESTS & MERGE (20 pts) ============
#
# On GitHub, for EACH of the 3 branches:
#
# 1. Go to the repository → Pull Requests → New Pull Request
# 2. base: main  ←  compare: fix/issue-X-<name>
# 3. Title: same as the commit message
# 4. Body: "Fixes #X. See commit message for details.
#           Tests re-run: all previously failing tests now pass."
# 5. Request a review from a team member (or review it yourself)
# 6. Approve and Merge (use "Merge pull request" or "Squash and merge")
# 7. Delete the branch after merge
#
# Do this for all 3 branches, one at a time:
#   fix/issue-1-subtract  →  merge into main
#   fix/issue-2-multiply  →  merge into main
#   fix/issue-3-divide    →  merge into main
#
# After all 3 are merged, pull locally and run the full suite:
#
#    git checkout main
#    git pull origin main
#    python -m pytest tests/ -v
#
# All 19 tests should pass.


# ======= PHASE 5 – FINALIZATION (10 pts) =====================
#
# 1. Verify on GitHub:
#    - All 3 issues are closed
#    - All 3 PRs are merged
#    - README.md is up-to-date and displays properly
#    - All code files contain docstrings and comments
#    - tests/ folder with its own README.md is present
#    - templates/README.md and static/README.md are present
#
# 2. Write the report (PDF, max 3 pages excluding cover page):
#    Cover page: project name, team number, members, date
#    The report must address each section of the lab:
#      - Repo setup (how you created the repo, added collaborators)
#      - Documentation (what was documented, why)
#      - Tests & issue tracking (how tests exposed bugs, issues created)
#      - Bug fixes & branch workflow (branch per issue, commits, test re-runs)
#      - Merge & final tests (PR process, final test results)
#      - Finalization (status of repo, lessons learned)
#
# 3. Make the repo PUBLIC before the deadline.
#
# 4. Submit:
#    a) GitHub repo link
#    b) Report PDF


# ============ APPENDIX A – BUGGY-BUT-DOCUMENTED operators.py =
#
# Paste this content into operators.py BEFORE making the initial
# commit to main, so that the bugs are present in the codebase
# and can later be fixed on dedicated branches.
#
# --- BEGIN FILE ---
"""operators.py — Arithmetic operator functions for the calculator.

Each function takes two numeric operands and returns the result of the
corresponding arithmetic operation.
"""


def add(a, b):
    """Return the sum of *a* and *b*.

    Args:
        a: First operand (number).
        b: Second operand (number).

    Returns:
        The sum a + b.
    """
    return a + b


def subtract(a, b):
    """Return the difference of *a* and *b*.

    Args:
        a: First operand (number).
        b: Second operand (number).

    Returns:
        The difference a - b.
    """
    return b - a


def multiply(a, b):
    """Return the product of *a* and *b*.

    Args:
        a: First operand (number).
        b: Second operand (number).

    Returns:
        The product a * b.
    """
    return a ** b


def divide(a, b):
    """Return the quotient of *a* divided by *b*.

    Args:
        a: Dividend (number).
        b: Divisor (number).  Must not be zero.

    Returns:
        The quotient a / b (true division).
    """
    return a // b
# --- END FILE ---


# ============ APPENDIX B – FIXED operators.py =================
#
# After all bugs are fixed (on their branches), the final
# operators.py should look like this:
#
# --- BEGIN FILE ---
# (same docstrings as above but with these function bodies:)
#   subtract:  return a - b
#   multiply:  return a * b
#   divide:    return a / b
# --- END FILE ---
