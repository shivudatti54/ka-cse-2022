# Arithmetic Operators in Java - Summary

## Key Definitions and Concepts

- **Binary Arithmetic Operators**: Operators that require two operands - addition (+), subtraction (-), multiplication (\*), division (/), and modulus (%)
- **Unary Operators**: Operators requiring single operand - increment (++) and decrement (--) with prefix and postfix forms
- **Compound Assignment Operators**: Shorthand operators combining arithmetic with assignment (+=, -=, \*=, /=, %=)
- **Type Promotion**: Automatic conversion of smaller numeric types to larger types during arithmetic operations

## Important Formulas and Behaviors

- Integer division truncates decimal part: `17 / 5 = 3`
- Modulus returns remainder: `17 % 5 = 2`
- Prefix: `++x` increments then uses value
- Postfix: `x++` uses value then increments
- byte, short, char always promoted to int in arithmetic
- Operators follow precedence: postfix → unary → multiplicative (\* / %) → additive (+ -)

## Key Points

- The + operator also performs string concatenation when either operand is a String
- Compound assignment operators automatically handle type casting
- All arithmetic operators are left-associative
- Division by zero throws ArithmeticException for integers
- Floating-point division by zero produces Infinity or NaN

## Common Mistakes to Avoid

1. Assuming `17 / 5` equals 3.4 (forgets integer division)
2. Confusing prefix and postfix increment behavior in expressions
3. Forgetting that byte/short operands are promoted to int
4. Using modulus operator incorrectly with negative numbers

## Revision Tips

1. Practice writing expressions with all operator types
2. Trace through prefix/postfix examples step by step
3. Remember the type promotion hierarchy: byte/short/char → int → long → float → double
4. Review previous year university questions on arithmetic operators for pattern understanding
