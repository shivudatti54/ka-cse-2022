# Cyclic Codes - Summary

## Key Definitions and Concepts

- **Cyclic Code**: A linear block code where any cyclic shift of a codeword yields another valid codeword.
- **Generator Polynomial g(x)**: The unique monic polynomial that generates all codewords; g(x) must divide xⁿ - 1, with degree r = n - k.
- **Parity Check Polynomial h(x)**: Satisfies g(x) · h(x) = xⁿ - 1; degree = k.
- **Syndrome s(x)**: The remainder when the received polynomial r(x) is divided by g(x); s(x) = 0 indicates valid codeword.

## Important Formulas and Theorems

- Codeword: c(x) = m(x) · g(x), where m(x) is the message polynomial of degree < k
- Systematic encoding: c(x) = xⁿ⁻ᵏ · m(x) + [xⁿ⁻ᵏ · m(x) mod g(x)]
- Error-correcting capability: t = ⌊(d - 1)/2⌋, where d is minimum distance
- Burst error detection: All bursts of length ≤ degree of g(x) are detected

## Key Points

- Cyclic codes are ideals in the ring GF(q)[x]/(xⁿ - 1), making algebraic treatment possible
- The generator polynomial is found by selecting a factor of xⁿ - 1 with appropriate degree
- Syndrome decoding exploits the cyclic structure to simplify error correction
- CRC codes are practical applications used in Ethernet, ZIP, PNG, and many communication protocols
- All cyclic codes are linear, but not all linear codes are cyclic
- Cyclic codes can be decoded efficiently using shift registers and feedback connections

## Common Mistakes to Avoid

- Forgetting that polynomial multiplication is performed modulo (xⁿ - 1), not ordinary multiplication
- Confusing systematic and non-systematic encoding methods and their resulting codeword formats
- Incorrectly computing the syndrome by using the wrong divisor polynomial
- Not reducing polynomial coefficients modulo the field characteristic (e.g., mod 2 for GF(2))

## Revision Tips

- Practice factorizing xⁿ - 1 for small n to find possible generator polynomials
- Work through at least 3-4 encoding and syndrome computation examples by hand
- Remember that the cyclic property means you only need to store one row of the generator matrix conceptually—the others are its cyclic shifts
- Review the connection to BCH codes as cyclic codes with designed minimum distance
