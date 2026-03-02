# Floating-Point Types - Summary

## Key Definitions and Concepts

- **Floating-Point Types**: Java primitive types used to represent real numbers with fractional parts, following IEEE 754 standard.
- **float**: 32-bit single-precision floating-point type with ~6-7 significant decimal digits.
- **double**: 64-bit double-precision floating-point type with ~15 significant decimal digits (DEFAULT for floating-point literals).
- **Floating-Point Literal**: Decimal number representation in Java code, defaulting to double unless suffixed with 'f' or 'F'.
- **IEEE 754**: International standard for floating-point arithmetic defining formats, operations, and special values.

## Important Formulas and Theorems

- **float range**: ±1.4 × 10⁻⁴⁵ to ±3.4 × 10³⁸ (approximately)
- **double range**: ±4.9 × 10⁻³²⁴ to ±1.8 × 10³⁰⁸ (approximately)
- **Precision**: float = 6-7 digits, double = 15 digits
- **Memory**: float = 32 bits (4 bytes), double = 64 bits (8 bytes)

## Key Points

- Floating-point literals in Java default to double type; use 'f' or 'F' suffix for float.
- The double type is preferred for most numerical computations due to superior precision.
- Special values: POSITIVE_INFINITY, NEGATIVE_INFINITY, and NaN (Not a Number).
- NaN comparisons always return false; use Double.isNaN() for testing.
- Widening conversion (float to double) is automatic; narrowing requires explicit casting.
- Floating-point arithmetic introduces rounding errors due to finite representation.
- Math class methods return double values by default.

## Common Mistakes to Avoid

1. **Forgetting float suffix**: Writing `float f = 3.14;` causes a compile error because 3.14 is a double literal. Use `3.14f`.

2. **Using == for NaN comparison**: NaN == NaN returns false. Always use `Double.isNaN(value)`.

3. **Ignoring precision loss**: Narrowing double to float loses significant precision; be aware of potential data loss.

4. **Assuming exact decimal representation**: Binary floating-point cannot exactly represent many decimal fractions (like 0.1), leading to subtle rounding errors.

## Revision Tips

1. Practice declaring variables with both decimal and scientific notation to reinforce literal syntax rules.

2. Write small programs to generate and detect special values (Infinity, NaN) to understand their behavior.

3. Remember the precision difference: 6-7 digits for float versus 15 digits for double.

4. Review type conversion rules, especially the automatic widening from float to double.

5. For exams, memorize the suffix requirement for float literals and the NaN comparison rule as frequently tested concepts.