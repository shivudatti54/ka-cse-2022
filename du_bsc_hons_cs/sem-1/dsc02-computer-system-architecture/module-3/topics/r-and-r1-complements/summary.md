# R and R-1 Complements - Summary

## Key Definitions and Concepts

- **R-1's Complement (Diminished Radix Complement):** For an n-digit number N in base R, it is (R^n - 1) - N. In binary, this is the 1's complement (flip all bits).
- **R's Complement (Radix Complement):** For an n-digit number N in base R, it is R^n - N. In binary, this is the 2's complement (add 1 to 1's complement).

## Important Formulas and Theorems

- **R-1's Complement Formula:** (R^n - 1) - N = (R-1)(R-1)(R-1)...(R-1) - N
- **R's Complement Formula:** R^n - N = (R-1's complement) + 1
- **Binary 1's complement:** Flip all bits (0→1, 1→0)
- **Binary 2's complement:** 1's complement + 1
- **2's complement range for n bits:** -2^(n-1) to +2^(n-1) - 1

## Key Points

- Complements simplify subtraction by converting it to addition
- 2's complement is the standard for signed number representation in modern computers
- 2's complement has a unique zero representation, unlike 1's complement
- Always discard the end carry when using R's complement method
- Add the end carry back when using R-1's complement method
- For binary: R-1 = 1, so 1's complement = 1 - each bit
- For decimal: R-1 = 9, so 9's complement = 9 - each digit

## Common Mistakes to Avoid

1. **Forgetting to discard/add carry:** Always handle the end carry according to the method used
2. **Confusing 1's and 2's complement:** 1's complement is just bit flipping; 2's complement requires adding 1
3. **Incorrect range calculation:** Remember the asymmetric range in 2's complement (more negative than positive values)
4. **Sign extension errors:** When extending to larger bit widths, replicate the sign bit for negative numbers

## Revision Tips

1. Practice converting between decimal and binary complements with various bit widths
2. Memorize the shortcut method: for 2's complement, find the rightmost 1 and flip all bits to its left
3. Solve at least 5 subtraction problems using both complement methods
4. Understand why 2's complement is preferred over 1's complement in computer systems
5. Review the relationship between complements and signed arithmetic overflow detection