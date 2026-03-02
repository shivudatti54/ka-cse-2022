# Identifiers, Keywords, and Literals - Summary

## Key Definitions and Concepts

- **Identifier**: A name given to a variable, function, class, or other user-defined entity in Python
- **Keyword**: Reserved words that have special meaning in Python (35 keywords in Python 3.12)
- **Literal**: A notation for representing a fixed value directly in source code

## Important Formulas and Theorems

- Identifier pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
- Binary literal prefix: `0b`
- Octal literal prefix: `0o`
- Hexadecimal literal prefix: `0x`
- Scientific notation: `aeb` means a × 10^b

## Key Points

1. Identifiers must start with a letter or underscore, not a digit
2. Python is case-sensitive: `num`, `Num`, and `NUM` are different
3. All 35 Python keywords cannot be used as identifiers
4. Keywords `True`, `False`, and `None` are capitalized differently from other keywords
5. Integer literals can be decimal, binary (0b), octal (0o), or hexadecimal (0x)
6. Float literals can use scientific notation (e.g., 1.5e10)
7. String literals use single or double quotes; triple quotes for multiline
8. Raw strings (r"...") treat backslashes as literal characters
9. Use snake_case for variables/functions, PascalCase for classes, UPPER_SNAKE_CASE for constants
10. `None` is not equivalent to `0`, `False`, or empty string

## Common Mistakes to Avoid

- Using keywords as variable names (causes SyntaxError)
- Starting identifiers with digits (e.g., `2name`)
- Using hyphens in identifiers (e.g., `my-variable` - Python interprets this as subtraction)
- Confusing `=` (assignment) with `==` (comparison)
- Using `==` to compare with `None` instead of `is None`

## Revision Tips

1. Practice identifying valid/invalid identifiers with 10+ examples
2. Memorize the complete list of 35 Python keywords
3. Write code demonstrating all types of literals
4. Remember naming conventions by heart - they frequently appear in exam questions
5. Use the `type()` function to verify literal types in Python interactive mode