# Representation of Integers - Summary

## Key Definitions and Concepts

- **Positional Number System:** A number system where each digit's value depends on its position and the base/radix (r). Value = Σ dᵢ × rⁱ

- **Binary (Base-2):** Uses digits 0,1; powers of 2; fundamental to digital computers

- **Octal (Base-8):** Uses digits 0-7; each digit = 3 binary bits

- **Hexadecimal (Base-16):** Uses digits 0-9, A-F; each digit = 4 binary bits

- **Two's Complement:** Standard signed number representation where negative numbers are obtained by inverting all bits and adding 1

## Important Formulas and Theorems

- **n-bit Unsigned Range:** 0 to (2ⁿ - 1)
- **n-bit Two's Complement Range:** -2ⁿ⁻¹ to +(2ⁿ⁻¹ - 1)
- **n-bit One's Complement/Sign-Magnitude Range:** -(2ⁿ⁻¹ - 1) to +(2ⁿ⁻¹ - 1)
- **Number of representable values in two's complement:** 2ⁿ (includes one zero)
- **Two's complement conversion:** Invert bits, add 1

## Key Points

- Two's complement is the universal standard for signed integers in modern computers due to natural arithmetic and single zero representation

- Binary to octal: Group bits in threes; Binary to hex: Group bits in fours

- Overflow in two's complement occurs when adding two positives gives negative, or two negatives gives positive

- One's complement requires end-around carry; two's complement simply discards overflow

- Sign-magnitude and one's complement have two zeros (problematic for arithmetic)

- Base conversion: Divide by target base repeatedly for decimal-to-any; use positional formula for any-to-decimal

## Common Mistakes to Avoid

1. **Forgetting overflow bit:** Always discard the carry out of the MSB in two's complement addition

2. **Wrong range calculation:** Remember two's complement has one more negative value than positive

3. **Two's complement of zero:** The two's complement of zero is still zero (not a problem—it's self-inversing)

4. **Sign extension confusion:** When extending to larger bit width, replicate the sign bit for two's complement

## Revision Tips

1. Practice 10+ conversion problems covering all base pairs until速度和准确性 become automatic

2. Memorize the range formulas for all three signed representations

3. Write out the two's complement conversion steps explicitly for negative numbers

4. Understand why two's complement simplifies hardware (same adder for addition/subtraction)

5. Review previous year DU exam questions on this topic for pattern and difficulty level