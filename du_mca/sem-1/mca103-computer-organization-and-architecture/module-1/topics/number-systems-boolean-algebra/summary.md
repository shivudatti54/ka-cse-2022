# Number Systems and Boolean Algebra - Summary

## Key Definitions and Concepts

- **Number Systems**: Decimal (base-10), Binary (base-2), Octal (base-8), Hexadecimal (base-16)
- **2's Complement**: Standard method for representing signed integers; positive numbers unchanged, negative obtained by complementing and adding 1
- **Boolean Algebra**: Algebra of binary variables with three basic operations: OR (+), AND (·), NOT (')
- **Logic Gates**: Hardware implementations of Boolean functions—NOT, AND, OR, NAND, NOR, XOR, XNOR
- **Universal Gates**: NAND and NOR gates that can implement any Boolean function alone

## Important Formulas and Theorems

- **De Morgan's Theorems**: (A + B)' = A' · B' and (A · B)' = A' + B'
- **Distributive**: A + (B · C) = (A + B) · (A + C); A · (B + C) = (A · B) + (A · C)
- **Absorption**: A + (A · B) = A; A · (A + B) = A
- **K-Map Grouping**: Variables that change within a group are eliminated; those that remain are kept

## Key Points

1. Each hexadecimal digit represents exactly 4 binary bits; each octal digit represents exactly 3 binary bits.

2. 2's complement representation eliminates the problem of duplicate zero found in sign-magnitude and 1's complement.

3. For n-bit 2's complement, the range is -2^(n-1) to +2^(n-1)-1.

4. Binary subtraction using 2's complement involves adding the 2's complement of the subtrahend.

5. XOR outputs 1 when inputs differ; XNOR outputs 1 when inputs are equal.

6. Larger K-map groups (size 2^n) yield simpler terms with fewer variables.

7. Don't-care conditions (X) in K-maps can be used to simplify expressions further.

## Common Mistakes to Avoid

1. Confusing when to use SOP vs POS—choose based on number of 1s vs 0s in truth table.

2. Forgetting that K-map groups must contain 1, 2, 4, 8, or 16 cells (powers of 2).

3. Not handling the carry bit correctly in 2's complement arithmetic.

4. Applying De Morgan's theorem incorrectly—remember to apply complement to the entire expression and each term.

5. Misplacing bits in K-map due to Gray code ordering (00, 01, 11, 10).

## Revision Tips

1. Practice at least 5 conversion problems daily until，速度 becomes automatic.

2. Create a truth table for De Morgan's theorems to memorize them visually.

3. Solve at least 3 K-map problems covering 2, 3, and 4 variables.

4. Remember: NAND = AND followed by NOT; NOR = OR followed by NOT.

5. In exams, always show your K-map setup—even if final answer is wrong, method marks are awarded.