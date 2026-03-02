# Primitive Types in Java - Summary

## Key Definitions and Concepts

- **Primitive Types**: The eight fundamental data types in Java that are not objects: byte, short, int, long, float, double, char, and boolean.

- **Widening Conversion**: Automatic type conversion from a smaller type to a larger type without data loss.

- **Narrowing Conversion**: Explicit conversion from a larger type to a smaller type using cast operator, with potential data loss.

- **Type Promotion**: Automatic promotion of operands in arithmetic operations to a larger type before computation.

## Important Formulas and Ranges

| Type   | Size   | Range                            |
| ------ | ------ | -------------------------------- |
| byte   | 8-bit  | -128 to 127                      |
| short  | 16-bit | -32,768 to 32,767                |
| int    | 32-bit | -2,147,483,648 to 2,147,483,647  |
| long   | 64-bit | ±9.22 × 10^18                    |
| float  | 32-bit | ±3.4 × 10^38 (approx 7 digits)   |
| double | 64-bit | ±1.8 × 10^308 (approx 15 digits) |
| char   | 16-bit | 0 to 65,535 (Unicode)            |

**Default Values**: byte, short, int, long = 0; float, double = 0.0; char = '\u0000'; boolean = false

## Key Points

- Java has exactly 8 primitive types, divided into integral (byte, short, int, long), floating-point (float, double), character (char), and boolean types.

- int is the default integer type; double is the default floating-point type in Java.

- char is unsigned and 16-bit, capable of holding Unicode characters.

- Local variables must be initialized before use; instance variables get default values.

- Widening conversions are automatic; narrowing conversions require explicit casting.

- Using 'L' suffix for long literals and 'f'/'F' suffix for float literals is mandatory.

- Underscores in numeric literals (Java 7+) improve readability without changing values.

## Common Mistakes to Avoid

1. **Forgetting the 'f' suffix** when declaring float literals—this causes compilation error as the literal is treated as double.

2. **Not using cast** when narrowing conversions are needed—this results in compilation error.

3. **Assuming boolean can be treated as integer**—unlike C/C++, Java boolean is strictly logical.

4. **Ignoring integer overflow**—Java does not warn about overflow; it wraps around silently.

5. **Confusing char with byte**—char is 16-bit unsigned, while byte is 8-bit signed.

## Revision Tips

1. Create a quick reference table of all primitive types with their sizes and ranges for quick recall.

2. Practice writing code that involves various type conversions to reinforce the concepts.

3. Remember the widening hierarchy: byte → short → int → long → float → double.

4. Review default values before the exam—they are frequently tested in multiple-choice questions.

5. Understand that char uses Unicode encoding, which allows international character sets beyond ASCII.
