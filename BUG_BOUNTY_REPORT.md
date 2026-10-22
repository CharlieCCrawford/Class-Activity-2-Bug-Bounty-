# Bug Bounty Report

| | |
|---|---|
| **Team name** | Charlie Crawford |
| **Program** | B: Student Grade Lookup |

## Bugs found

1. **Missing colon after `if name in grades`:** `SyntaxError`, so the program won't run.
2. **Missing colon after `else`:** another `SyntaxError`.
3. **`sum(grades)` adds the dictionary keys (names) instead of the scores:** `TypeError` on the average line. Fix: `sum(grades.values())`.
4. **Possible crash with an empty dictionary:** if `grades` were `{}`, `len(grades)` is 0 and the average line raises `ZeroDivisionError`. This is a hidden bug that doesn't happen with the current data.

## Which bugs did the AI find?

It found bugs 1, 2 and 3 in its first answer and explained each one, including that bug 2 only shows up after bug 1 is fixed. It found bug 4 only later, when asked about edge cases.

## Which did it miss?

It missed the empty-dictionary `ZeroDivisionError` (bug 4) in the first review. In the first answer it also treated case sensitivity and extra spaces in the input as "optional improvements" rather than bugs, even though they mean a real student like "alice" isn't found.

## One thing the AI did well

It explained *why* each bug happens, not just how to fix it. For example, summing a dictionary uses its keys, and it showed the exact `TypeError` message. It also gave example output so the fixes could be checked.

## One thing the AI missed or got wrong

- **It contradicted itself.** It first suggested `.title()` to make name lookup more forgiving. Later it said `.title()` breaks names like "McDonald" and switched to `.casefold()`.
- **It created a style problem and then "fixed" it.** The commented version split the `if`/`else` with a blank line and comments. The PEP 8 step then listed removing that as a style fix.
- **It didn't run a style checker until the code was pushed to GitHub.** Before that it said "no PEP 8 violations that I can see".

## Style improvements the AI made (PEP 8)

- Added a module docstring and, later, function docstrings.
- Renamed the constant `grades` to `GRADES` (module-level constants in capitals).
- Fixed blank-line use: kept `if`/`else` together, used single blank lines between logical sections and two blank lines between top-level functions.
- Removed the out-of-date "FIX" comments.
- Good practice beyond PEP 8: a more descriptive name (`student_name`), a separate `class_average` variable, logic in functions with an `if __name__ == '__main__':` guard.

## Style issues the AI missed

- **Lines too long in the commented version:** running `pycodestyle` on `code/2_fixed.py` found 4 comment lines over the 79-character limit (E501). The AI had said the code had "short lines".
- **It didn't suggest functions or a `__main__` guard until asked.**
- **The final version mixes output styles:** `print(match, 'scored', GRADES[match])` with commas next to an f-string. `print(f'{match} scored {GRADES[match]}')` would be more consistent.
- **Some changes were labelled "PEP 8" when the link is loose:** removing comments and splitting the average onto its own line are good habits, not strict PEP 8 rules.
