# C Programming Data Types - Summary

## Key Definitions and Concepts

- **Data Type**: A classification that specifies which type of value a variable can hold and determines the operations that can be performed on it.

- **Primary Data Types**: Fundamental data types in C including int (integers), float (single-precision decimals), double (double-precision decimals), char (characters), and void (no value).

- **Type Modifiers**: Keywords that alter the characteristics of basic types: signed/unsigned and short/long.

- **Derived Data Types**: Types constructed from primary types: arrays, pointers, structures, and unions.

- **Type Conversion**: The process of converting one data type to another, occurring implicitly or explicitly through casting.

## Important Formulas and Theorems

- **Signed Integer Range**: -2^(n-1) to 2^(n-1)-1, where n is the number of bits
- **Unsigned Integer Range**: 0 to 2^n - 1
- **sizeof(char)**: Always returns 1 byte
- **Type Conversion Hierarchy**: char → int → long → float → double (implicit promotion)

## Key Points

- On most systems, int occupies 4 bytes, float occupies 4 bytes, and double occupies 8 bytes.

- The unsigned modifier doubles the positive range by eliminating negative values.

- The void data type indicates absence of type and is used for function returns, parameters, and generic pointers.

- Implicit conversion automatically promotes smaller types to larger types to prevent data loss.

- Explicit type casting uses the syntax (target_type)expression and is performed by the programmer.

- Integer division (int/int) always produces an integer result, discarding the fractional part.

- Floating-point literals without suffix are of double type by default in C.

- Character data type stores ASCII values, allowing arithmetic operations on characters.

## Common Mistakes to Avoid

1. **Assuming integer division produces decimal results**: Remember that 5/2 = 2, not 2.5. Cast at least one operand to float for decimal results.

2. **Forgetting that char is numeric**: Characters store ASCII codes, so 'A' + 1 = 66, not a compilation error.

3. **Not using the correct suffix for long literals**: Always use 'L' for long integer literals to avoid overflow warnings.

4. **Confusing %d and %u format specifiers**: Use %d for signed integers and %u for unsigned integers in printf statements.

5. **Incorrect void pointer usage**: Remember that void* requires explicit casting before dereferencing in most contexts.

## Revision Tips

1. Practice writing programs that demonstrate sizeof operator with all data types to memorize standard sizes.

2. Create a table mapping data types to their typical sizes and ranges for quick reference during exams.

3. Solve multiple choice questions on type conversion to strengthen understanding of implicit promotion rules.

4. Review previous years' question papers to identify the pattern of questions asked on data types (typically 2-4 questions).

5. Implement small programs demonstrating integer vs. floating-point operations to understand practical implications of data type selection.