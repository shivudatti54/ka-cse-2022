# Floating-Point Types - Summary

## Key Definitions and Concepts

- FLOAT: 32-bit single-precision floating-point type, approximately 6-7 significant decimal digits
- DOUBLE: 64-bit double-precision floating-point type, approximately 15-16 significant decimal digits
- IEEE 754: International standard for floating-point arithmetic defining representation, operations, and special values
- MANTISSA (SIGNIFICAND): The significant digits of a floating-point number, stored in binary
- NAN (NOT A NUMBER): Special value resulting from invalid operations like sqrt(-1) or 0.0/0.0
- INFINITY: Special value from operations like division by zero or overflow

## Important Formulas and Theorems

- Float range: ±1.4 × 10^-45 to ±3.4 × 10^38
- Double range: ±4.9 × 10^-324 to ±1.8 × 10^308
- Precision comparison: double has ~2× the precision bits (52 vs 23) of float
- Tolerance comparison: |a - b| < epsilon (never use == for floating-point)

- All floating-point literals with## Key Points

 decimal points default to double; use f or F suffix for float
- Double is the DEFAULT choice for numerical computations due to higher precision
- Floating-point uses BINARY representation, causing imprecise representation of common decimal fractions like 0.1
- Special values Infinity and NaN are handled via Double.isInfinite() and Double.isNaN() methods
- Automatic promotion: float promotes to double in mixed-type expressions
- Explicit casting required when converting from double to float
- Integer division (/) vs floating-point division depends on operand types

## Common Mistakes to Avoid

- Forgetting the 'f' suffix when declaring float literals, causing compilation errors
- Using == to compare floating-point numbers, which fails due to precision issues
- Assuming floating-point arithmetic is exact like mathematical real numbers
- Dividing integers where floating-point division was intended (5/2 gives 2, not 2.5)
- Not handling special values (NaN, Infinity) when performing mathematical operations

## Revision Tips

- Practice writing both float and double declarations with various literal formats
- Remember: float = 32-bit, double = 64-bit, double is more precise
- Always use tolerance-based comparison for floating-point equality
- Review the Math class methods for common numerical operations
- Understand why 0.1 + 0.2 ≠ 0.3 in floating-point—practice explaining this concept