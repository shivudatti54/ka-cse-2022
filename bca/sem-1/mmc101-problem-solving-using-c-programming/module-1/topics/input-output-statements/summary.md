# Input Output Statements in C Programming - Summary

## Key Definitions and Concepts

- **Standard I/O Library (stdio.h)**: Header file containing functions for input and output operations in C
- **Standard Streams**: stdin (keyboard), stdout (monitor), stderr (error output) - automatically opened at program start
- **Format String**: String containing literal text and format specifiers that control output/input formatting
- **Format Specifiers**: % symbols that indicate data type and formatting (e.g., %d for int, %f for float, %s for string)
- **Escape Sequences**: Backslash combinations (\n, \t, \\, etc.) that produce special characters

## Important Formulas and Theorems

- **printf() Syntax**: `printf("format string", arg1, arg2, ...);`
- **scanf() Syntax**: `scanf("format string", &var1, &var2, ...);`
- **ASCII Conversion**: Uppercase = Lowercase - 32 (e.g., 'A' = 'a' - 32)

## Key Points

- Always include '#include <stdio.h>' at the top of programs using I/O functions
- Use & (address-of operator) with scanf() for variables, but NOT for string arrays
- Format specifiers: %d (int), %f (float), %lf (double), %c (char), %s (string), %p (pointer)
- Width specifier: %5d creates 5-character field; %.2f limits to 2 decimal places
- getchar() returns int to accommodate EOF; always store in int variable
- \n creates new line, \t creates tab, \\ creates backslash character
- scanf() returns number of successfully read items - useful for validation
- Use fgets() instead of gets() to prevent buffer overflow vulnerabilities

## Common Mistakes to Avoid

- Forgetting to include stdio.h header file
- Missing the ampersand (&) in scanf() for non-array variables
- Using wrong format specifier (e.g., %d for float, %f for int)
- Not checking scanf() return value for input validation
- Using gets() instead of fgets() for string input (buffer overflow risk)

## Revision Tips

- Practice writing printf() statements with different format specifiers and width/precision modifiers
- Memorize common format specifiers: d/i (integer), f (float), c (char), s (string)
- Remember that character input functions (getchar) return int, not char
- Review the ASCII table values for uppercase/lowercase letter conversion
- Write programs that take user input, process it, and display formatted output