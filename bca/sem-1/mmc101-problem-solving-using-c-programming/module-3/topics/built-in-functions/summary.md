# Built In Functions in C - Summary

## Key Definitions and Concepts

- **Built-in functions**: Pre-defined functions provided by the C standard library that perform common operations without requiring custom implementation
- **Header files**: Files containing function prototypes and definitions that must be included using #include directive before using library functions
- **Library functions**: Another term for built-in functions, organized into categories based on functionality

## Important Functions by Category

**I/O Functions (stdio.h)**: printf(), scanf(), getchar(), putchar(), gets(), puts()

**String Functions (string.h)**: strlen(), strcpy(), strcat(), strcmp(), strrev(), strupr(), strlwr()

**Math Functions (math.h)**: sqrt(), pow(), abs(), fabs(), ceil(), floor(), sin(), cos(), tan()

**Character Functions (ctype.h)**: isalpha(), isdigit(), isupper(), islower(), toupper(), tolower()

**Memory Functions (stdlib.h)**: malloc(), calloc(), realloc(), free()

**Utility Functions (stdlib.h)**: atoi(), atol(), atof(), exit()

## Key Points

- ALWAYS include the correct header file before using any built-in function

- printf() uses format specifiers (%d, %f, %c, %s) for output; scanf() requires address of variables using &

- strlen() returns length excluding null character; strcpy() copies including null character

- strcmp() returns 0 for equal strings, negative if first < second, positive if first > second

- abs() works with integers; fabs() is for floating-point values

- isalpha() returns true for both uppercase and lowercase letters

- malloc() allocates raw memory; calloc() allocates and initializes to zero

- Always check malloc() return value for NULL before using allocated memory

- Never use == to compare strings; use strcmp() instead

- String manipulation functions require character arrays, not string literals

## Common Mistakes to Avoid

1. Forgetting to include header files before using functions

2. Using abs() instead of fabs() for floating-point numbers

3. Forgetting the ampersand (&) with scanf() for non-array variables

4. Using == operator instead of strcmp() for string comparison

5. Not allocating enough space for string manipulation functions (causing buffer overflow)

6. Using gets() which does not check buffer length (use fgets() instead)

7. Not freeing dynamically allocated memory causing memory leaks

## Revision Tips

1. Practice writing programs that combine multiple string functions together

2. Memorize which header file corresponds to which category of functions

3. Understand the return types and parameters of commonly used functions

4. Practice with examples of string reversal, palindrome checking, and case conversion

5. Review previous year question papers to understand exam patterns and frequently asked programs