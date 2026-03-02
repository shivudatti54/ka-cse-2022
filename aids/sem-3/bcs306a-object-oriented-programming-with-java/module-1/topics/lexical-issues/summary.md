# Lexical Issues in Java - Summary

## Key Definitions and Concepts

- **Token**: The smallest meaningful unit in a Java program, including identifiers, keywords, literals, operators, and separators.
- **Unicode**: A character encoding standard that assigns unique numeric values (code points) to characters from virtually all writing systems.
- **Identifier**: A name given to program elements (variables, methods, classes) that must begin with a letter, $, or \_, and cannot be a Java keyword.
- **Literal**: A constant value written directly in source code (42, 3.14, 'A', "Hello", true).
- **Lexical Analysis**: The first phase of compilation where source code characters are converted into tokens.

## Important Formulas and Theorems

- **Character encoding**: `char` in Java is 16-bit UTF-16, supporting characters from the Basic Multilingual Plane directly and surrogate pairs for characters outside it.
- **Integer literal bases**: Decimal (base 10), Hexadecimal (0x prefix), Octal (0 prefix), Binary (0b prefix).
- **Operator Precedence**: Highest to lowest - Postfix → Unary → Multiplicative → Additive → Shift → Relational → Equality → Bitwise AND → Bitwise XOR → Bitwise OR → Logical AND → Logical OR → Ternary → Assignment.

## Key Points

- Java uses Unicode, allowing international character support in identifiers and string literals.
- Scanner provides convenient methods for parsing but is slower than BufferedReader for large inputs.
- BufferedReader with InputStreamReader is the most efficient standard input method for competitive programming.
- Identifiers are case-sensitive and cannot be Java reserved words.
- Integer literals without suffixes are int by default; floating-point literals without suffixes are double.
- Unicode escape sequences (\uXXXX) are processed during compilation before lexical analysis.
- Comments (//, /\* _/, /\*\* _/) are ignored by the compiler and cannot be nested.
- White space separates tokens but is significant within string and character literals.

## Common Mistakes to Avoid

1. **Forgetting to close Scanner resources** - Always call scanner.close() or use try-with-resources.
2. **Mixing nextInt() with nextLine()** - The newline remains in buffer, causing unexpected empty strings.
3. **Using lowercase 'l' in long literals** - It looks like the digit '1'; use uppercase 'L' instead.
4. **Treating floating-point literals as float without suffix** - Results in double type, causing compilation errors when assigning to float variables.
5. **Trying to use keywords as identifiers** - Cannot use words like 'class', 'public', 'void' as variable names.

## Revision Tips

1. Practice writing programs that use both Scanner and BufferedReader for input to understand their differences.
2. Memorize the different literal formats and their prefixes/suffixes for quick recognition.
3. Remember the operator precedence order or use parentheses to make expressions explicit.
4. Review past university exam questions on lexical analysis to understand the pattern of questions.
5. Create a checklist of valid identifier rules and verify them with code examples.
