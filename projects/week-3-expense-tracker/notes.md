## Session 2 — Bugs I Fixed

**Bug 1: `isformat` vs `isoformat`**
Python told me that there is an error regarding the syntax and suggested the proper syntax which is the 'isoformat'. After doing the suggested action the error was gone.

**Bug 2: `list_expenses` vs `list_expenses()`**
list_expenses is the object name, while list_expenses() is the function call. This distinction matters when referencing the object by name rather than instantiating the particular function, because the object does not yet exist.