# Logic Gates and Boolean Algebra - Summary

## Key Definitions and Concepts

- **Logic Gates:** Electronic circuits that implement Boolean functions; the fundamental building blocks of digital systems
- **Boolean Algebra:** Mathematical system for analyzing and simplifying digital circuits using binary variables (0 and 1)
- **Universal Gates:** NAND and NOR gates capable of implementing any Boolean function alone
- **Minterm:** Product term containing all variables (either true or complemented) where function equals 1
- **Maxterm:** Sum term containing all variables where function equals 0

## Important Formulas and Theorems

- **De Morgan's Theorems:** (A + B)' = A' · B' and (AB)' = A' + B'
- **Distributive:** A + BC = (A + B)(A + C)
- **Absorption:** A + AB = A and A(A + B) = A
- **K-map Grouping:** Groups of 2ⁿ cells (1,2,4,8...) eliminate n variables

## Key Points

1. AND, OR, NOT are basic gates; NAND and NOR are universal gates
2. XOR outputs 1 when inputs differ; XNOR outputs 1 when inputs are same
3. Boolean algebra uses +, ·, and ' for OR, AND, and NOT operations
4. Canonical SOP uses minterms (Σm); canonical POS uses maxterms (ΠM)
5. K-maps enable visual simplification of Boolean expressions
6. Minimization reduces circuit cost, complexity, and propagation delay
7. Any function can be realized using only NAND or only NOR gates

## Common Mistakes to Avoid

1. Confusing '+' with arithmetic addition—it's Boolean OR operation
2. Treating XOR same as OR—XOR gives 1 only for odd number of 1s
3. Making groups that are not powers of 2 when using K-maps
4. Forgetting that K-map cells must differ by only one variable horizontally/vertically
5. Not considering don't care conditions when simplifying

## Revision Tips

1. Practice drawing truth tables for all seven gates until automatic
2. Solve at least 5 K-map problems covering 2, 3, and 4 variables
3. Memorize De Morgan's theorems—they are most frequently tested
4. Practice implementing the same function using NAND only, then NOR only
5. Time yourself solving Boolean simplification problems for exam speed