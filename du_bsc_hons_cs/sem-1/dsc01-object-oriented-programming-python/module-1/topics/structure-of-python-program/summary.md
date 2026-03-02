# Structure of Python Program - Summary

## Key Definitions and Concepts

- **Python Interpreter**: The program that reads and executes Python source code, compiling it to bytecode first.

- **Indentation**: Whitespace at the beginning of lines used to define code blocks in Python; unlike other languages, Python uses indentation structurally.

- **Module**: A Python file containing definitions and statements, identified by the `.py` extension.

- **`__name__` variable**: A built-in attribute that equals `"__main__"` when a file is run directly, or the module name when imported.

- **Statement**: An instruction that performs an action (e.g., assignment, print).

- **Expression**: A combination that evaluates to a value (e.g., `5 + 3`, `x * 2`).

- **Docstring**: A string literal in triple quotes used for documenting modules, functions, and classes.

## Important Formulas and Concepts

- **Import statement syntax**: `import module_name` or `from module_name import name`
- **Indentation standard**: 4 spaces (or 1 tab) per level
- **Main block check**: `if __name__ == "__main__":`

## Key Points

- Python uses indentation rather than braces to define code blocks; incorrect indentation causes errors.

- Every Python file is a module; the filename (minus .py) becomes the module name.

- The `if __name__ == "__main__"` construct distinguishes between direct execution and module import.

- Python is dynamically typed—variables don't need explicit type declarations.

- Comments (using #) are ignored by the interpreter; docstrings are stored in `__doc__` attributes.

- The Python import system searches: current directory → standard library → site-packages.

- Multi-line statements can use parentheses, brackets, or backslash continuation.

- Python is case-sensitive; `print` and `Print` are treated differently.

## Common Mistakes to Avoid

- Mixing tabs and spaces for indentation—this causes confusing IndentationErrors.
- Forgetting to import modules before using their functions.
- Using incorrect module names or forgetting the `.py` extension is not used in imports.
- Not understanding that expressions produce values while statements perform actions.
- Writing code outside proper code blocks (indentation levels).

## Revision Tips

- Practice writing simple Python programs focusing on proper indentation from the start.
- Always use 4 spaces for indentation rather than tabs to avoid cross-platform issues.
- Review past DU exam questions on Python basic structure to understand the exam pattern.
- Memorize the exact syntax of the `if __name__ == "__main__"` construct.
- Write comments and docstrings in your code regularly to develop the habit.