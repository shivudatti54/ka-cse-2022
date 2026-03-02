# Constants And Keywords - Summary

## Key Definitions and Concepts

- **Constant**: A fixed value that does not change during program execution. Constants can be integer, floating-point, character, or string types.

- **Keyword**: A reserved word in C that has special meaning and cannot be used as an identifier. Examples include int, if, while, for, const, and return.

- **Symbolic Constant**: A named constant created using #define or const, making code more readable and maintainable.

- **Escape Sequence**: A backslash character combination (\n, \t, \\, etc.) representing special characters in C.

- **Enum**: A keyword used to define a set of named integer constants, useful for creating related constant values.

## Important Formulas and Theorems

- **Default enum values**: If not explicitly assigned, enum constants start at 0 and increment by 1.
- **Octal constants**: Must start with 0 (e.g., 077)
- **Hexadecimal constants**: Must start with 0x or 0X (e.g., 0xFF)
- **Constant suffixes**: U = unsigned, L = long, F = float

## Key Points

- C has 32 keywords in C89/C90, with 5 more in C99 and 5 in C11
- Integer constants can be written in decimal (base 10), octal (base 8), or hexadecimal (base 16)
- Floating-point constants default to double type unless suffixed with F or L
- Character constants use single quotes ('A'), while string literals use double quotes ("A")
- #define creates macros (text substitution), const creates actual variables with type safety
- Enum constants are of type int and can be assigned specific values
- Keywords cannot be redeclared or used as variable, function, or label names
- Escape sequence \0 represents the null character that terminates strings

## Common Mistakes to Avoid

- Using keywords as variable names, which causes compilation errors
- Confusing single quotes for characters with double quotes for strings
- Forgetting that #define does not allocate memory or perform type checking
- Using 0-prefixed numbers without realizing they are octal (e.g., 012 = decimal 10)
- Not remembering that character constants like 'A' are actually of type int, not char

## Revision Tips

1. Create a table of all C keywords and categorize them (data types, control flow, storage classes)
2. Practice writing programs using #define and const to understand their differences
3. Memorize common escape sequences and their meanings
4. Review previous DU question papers to identify the pattern of questions on constants and keywords
5. Write sample code demonstrating all types of constants to reinforce understanding