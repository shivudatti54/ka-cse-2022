# Syntax and Semantics in Python - Summary

## Key Definitions and Concepts

- **Syntax**: The set of rules defining valid program structure in Python (indentation, colons, statements)
- **Semantics**: The meaning and behavior of syntactically correct Python code
- **Dynamic Typing**: Variable types are determined at runtime; no explicit type declaration required
- **Namespace**: A dictionary mapping names to objects; Python has built-in, global, and local namespaces
- **LEGB Rule**: Order of scope resolution—Local → Enclosing → Global → Built-in

## Important Formulas and Operators

- **Arithmetic**: +, -, *, /, //, %, **
- **Comparison**: ==, !=, <, >, <=, >=
- **Logical**: and, or, not
- **Assignment**: =, +=, -=, *=, /=, //=, %=, **=

## Key Points

1. Python uses indentation (4 spaces or 1 tab) to define code blocks, not braces
2. Every compound statement (if, for, def, class) must end with a colon (:)
3. Python is case-sensitive; keywords cannot be used as variable names
4. Variables are created when assigned; no declaration needed
5. type() returns an object's data type; isinstance() checks type membership
6. f-strings provide modern string formatting: f"Value: {variable}"
7. input() always returns a string; conversion functions (int(), float()) needed for numeric input
8. The global keyword allows modification of global variables inside functions

## Common Mistakes to Avoid

- Using = instead of == in conditions (syntax error)
- Forgetting colons after control statements
- Incorrect indentation causing IndentationError
- Mixing tabs and spaces (use consistent indentation)
- Trying to modify global variables without declaring them as global

## Revision Tips

1. Practice writing if-elif-else and loop structures with proper indentation
2. Memorize operator precedence order or use parentheses liberally
3. Draw namespace diagrams to understand variable scope
4. Write small programs to test dynamic typing behavior
5. Review previous year examination questions on Python basics