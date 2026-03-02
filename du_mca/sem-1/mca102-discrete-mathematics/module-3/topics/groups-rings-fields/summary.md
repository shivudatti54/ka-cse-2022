# Groups, Rings, and Fields - Summary

## Key Definitions and Concepts
- **Group**: Set + single associative operation with identity and inverses
- **Ring**: Set with two operations (+, ⋅) where (+, ⋅) is a monoid and + is abelian
- **Field**: Commutative ring where all non-zero elements have multiplicative inverses
- **Subgroup**: Subset closed under group operation
- **Ideal**: Special subset in rings used to construct quotient rings

## Important Formulas and Theorems
- **Lagrange’s Theorem**: Order of subgroup divides order of finite group
- **Fermat’s Little Theorem**: a^(p-1) ≡ 1 mod p (for prime p, a≠0)
- **GF(pⁿ) Construction**: Use irreducible polynomials of degree n over GF(p)
- **Euler’s Totient Function**: φ(n) = |ℤₙ*|

## Key Points
- All fields are rings, but not vice versa
- ℤₙ is a field ⇨ n is prime
- Matrix rings are generally non-commutative
- GF(2ⁿ) elements can be represented as binary polynomials
- Homomorphisms preserve structure; isomorphisms show equivalence
- The additive group of a field is always abelian
- RSA relies on the multiplicative group ℤₙ* where n=pq

## Common Mistakes to Avoid
- Assuming all rings have multiplicative inverses (only fields do)
- Confusing group identity elements (e.g., additive vs multiplicative in rings)
- Forgetting to check commutativity for abelian groups/fields
- Misapplying GF(2ⁿ) arithmetic as standard integer operations

## Revision Tips
1. Practice axiom checks using ℤₙ, matrices, and polynomial sets
2. Create flashcards for definitions of groups/rings/fields
3. Solve past DU papers on GF(2ⁿ) construction and homomorphism problems
4. Implement GF(256) multiplication in Python to reinforce concepts

Length: 650 words