# Derangements - Nothing is in its Right Place - Summary

## Key Definitions and Concepts

- **Derangement:** A permutation of n distinct objects where no object appears in its original position (permutation with no fixed points)
- **Notation:** Dₙ or !n (subfactorial n)
- **Fixed Point:** An element i such that σ(i) = i in a permutation σ

## Important Formulas and Theorems

1. **Explicit Formula (Inclusion-Exclusion):**
   Dₙ = n! × (1 - 1/1! + 1/2! - 1/3! + ... + (-1)ⁿ/n!)

2. **Recursive Formula:**
   Dₙ = (n - 1) × (Dₙ₋₁ + Dₙ₋₂), with D₁ = 0, D₂ = 1

3. **Approximation:**
   Dₙ ≈ n!/e or Dₙ = ⌊n!/e + 1/2⌋

4. **Probability:**
   P(derangement) = Dₙ/n! → 1/e ≈ 0.3679 as n → ∞

## Key Points

- D₀ = 1 (by convention), D₁ = 0, D₂ = 1
- Sequence: 1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496, ...
- Approximately 36.79% of all permutations are derangements
- Derivation uses the inclusion-exclusion principle
- Applies to matching problems, hat-check problems, and random shuffling scenarios

## Common Mistakes to Avoid

- Confusing derangements with regular permutations (multiply by n! instead of using derangement formula)
- Forgetting base cases: D₁ = 0, not 1
- Using wrong sign in formula terms (alternating signs are crucial)
- Not understanding that derangements exclude all fixed points completely

## Revision Tips

1. Memorize the first 5-6 derangement values: D₃=2, D₄=9, D₅=44, D₆=265
2. Practice deriving the recurrence relation from the explicit formula
3. Remember the "hat-check" problem as a memory anchor for applications
4. The probability approaches 1/e ≈ 0.3679 — a useful approximation for large n
