# Data Representation and Arithmetic Operations - Summary

## Key Definitions and Concepts

- **Number Systems:** Decimal (base-10), Binary (base-2), Octal (base-8), Hexadecimal (base-16)
- **2's Complement:** Standard method for representing signed integers; single zero representation; range for n-bits: -2^(n-1) to +2^(n-1)-1
- **IEEE 754:** Standard for floating-point representation; single precision uses 1+8+23 bits; double precision uses 1+11+52 bits
- **Bias:** 127 for single precision, 1023 for double precision (actual exponent = stored - bias)
- **BCD (Binary Coded Decimal):** Represents each decimal digit with 4 binary bits

## Important Formulas and Theorems

- Binary to Decimal: Σ(b × 2^i) where b is each bit and i is its position
- 2's Complement: Invert all bits, then add 1
- Signed Range (2's complement): -2^(n-1) ≤ N ≤ 2^(n-1) - 1
- Unsigned Range: 0 ≤ N ≤ 2^n - 1
- Floating Point: (-1)^S × 1.F × 2^(E-bias)

## Key Points

- Computers use binary (base-2) internally; hex and octal are shorthand notations
- 2's complement is preferred over sign-magnitude and 1's complement due to simpler arithmetic
- Binary addition follows rules: 1+1=0 with carry; overflow detection differs for signed/unsigned
- IEEE 754 normalized numbers have implicit leading 1 in mantissa
- Special floating-point values exist for zero, infinity, NaN, and denormalized numbers
- Floating-point representation trades off range for precision
- BCD provides exact decimal representation but wastes storage space

## Common Mistakes to Avoid

- Forgetting to discard the carry bit when performing 2's complement subtraction
- Confusing the bias (127/1023) with the actual exponent value in floating-point
- Not normalizing the mantissa correctly when converting to floating-point
- Misidentifying overflow conditions in signed arithmetic (carry into MSB ≠ carry out)
- Ignoring the implicit 1 in IEEE 754 mantissa representation

## Revision Tips

1. Practice conversions between all four number systems until they become automatic
2. Memorize the 2's complement process and be able to perform it in both directions
3. Review IEEE 754 format components and special case bit patterns
4. Solve at least 5-10 problems from previous year DU question papers on this topic
5. Create a quick reference sheet with formulas and common binary patterns (powers of 2)