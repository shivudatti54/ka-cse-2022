# Floating-Point Types - Summary

## Key Definitions and Concepts

- **Floating-Point Types**: Java primitive types (float and double) for representing real numbers with decimal fractions
- **float**: 32-bit single-precision type with ~6-7 significant decimal digits
- **double**: 64-bit double-precision type with ~15 significant decimal digits
- **Mantissa (Significand)**: The significant digits of a floating-point number (23 bits for float, 52 bits for double)
- **Exponent**: The power of 2 by which the mantissa is scaled (8 bits for float, 11 bits for double)
- **NaN**: Special value representing "Not a Number," result of invalid operations like 0.0/0.0
- **IEEE 754**: International standard for floating-point arithmetic in modern computers

## Important Formulas and Theorems

- Float range: 1.4 × 10^-45 to 3.4 × 10^38 (positive values)
- Double range: 4.9 × 10^-324 to 1.8 × 10^308 (positive values)
- Float precision: approximately 7 decimal digits
- Double precision: approximately 15 decimal digits

## Key Points

- Floating-point literals default to double type; float requires 'f' or 'F' suffix
- double provides better precision and is preferred for most calculations
- Floating-point arithmetic involves inherent precision limitations and rounding errors
- Special values include: POSITIVE_INFINITY, NEGATIVE_INFINITY, NaN, +0.0, -0.0
- Automatic widening conversion from float to double; narrowing requires explicit cast
- Use tolerance-based comparison instead of == for floating-point equality
- Scientific notation uses E or e: 1.5e10 means 1.5 × 10^10
- For financial applications requiring exact decimal math, use BigDecimal instead

## Common Mistakes to Avoid

1. Forgetting the 'f' suffix when initializing float variables—this causes compile error
2. Comparing floating-point numbers using == operator—leads to unexpected results
3. Assuming floating-point can represent all decimal numbers exactly—0.1 + 0.2 ≠ 0.3
4. Using float for precision-critical calculations—double should be preferred
5. Not handling NaN and Infinity in numerical computations—these propagate through calculations

## Revision Tips

1. Practice writing floating-point literals with both decimal and scientific notation
2. Remember the suffix rule: float needs 'f', double is default (optional 'd')
3. Review the precision difference by running loops that accumulate small values
4. Understand why financial calculations should not use double/float
5. Know how to check for special values: Double.isNaN(), Double.isInfinite()