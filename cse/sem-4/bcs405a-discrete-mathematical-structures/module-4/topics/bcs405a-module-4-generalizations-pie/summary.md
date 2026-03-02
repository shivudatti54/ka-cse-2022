# Generalizations of the Principle of Inclusion-Exclusion - Summary

## Key Definitions and Concepts

- **Principle of Inclusion-Exclusion (PIE)**: A counting technique for finding the size of the union of sets by alternately adding and subtracting intersections of increasing cardinality.

- **Derangement (Subfactorial)**: A permutation where no element appears in its original position. Denoted Dₙ or !n.

- **Surjective/Onto Function**: A function where every element in the codomain is mapped to by at least one element in the domain.

- **Rook Polynomial**: A generating function R(B,x) = Σ rₖ(B)xᵏ where rₖ(B) counts k non-attacking rook placements on board B.

## Important Formulas and Theorems

**Generalized PIE for n sets:**
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| - Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| - ... + (-1)ⁿ⁻¹|A₁ ∩ ... ∩ Aₙ|

**Derangement formula:**
Dₙ = n! × Σ(k=0 to n) (-1)ᵏ/k! ≈ n!/e

**Derangement recurrence:**
Dₙ = (n-1)(Dₙ₋₁ + Dₙ₋₂), with D₀ = 1, D₁ = 0

**Onto functions (m to n, m ≥ n):**
nᵐ - C(n,1)(n-1)ᵐ + C(n,2)(n-2)ᵐ - ... + (-1)ⁿ⁻¹C(n,n-1)(1)ᵐ

## Key Points

- The inclusion-exclusion principle handles overcounting in unions by subtracting intersections, adding back triple intersections, and continuing the alternating pattern.
- For n sets, there are 2ⁿ - 1 non-empty terms in the inclusion-exclusion formula (excluding the empty intersection).
- The complement form |A'| = |U| - |A| is often easier when counting elements avoiding properties.
- Derangements Dₙ approach n!/e as n increases, with D₄ = 9, D₅ = 44, D₆ = 265.
- Onto functions from m elements to n elements equals n! × S(m,n), where S(m,n) is a Stirling number of the second kind.
- Rook polynomials provide an alternative to direct inclusion-exclusion for board problems with many restrictions.

## Common Mistakes to Avoid

- **Wrong LCM in divisibility problems**: Always use the least common multiple when computing intersections of divisibility sets.
- **Forgetting alternating signs**: The sign pattern must alternate starting with positive for single sets.
- **Missing terms**: Remember that the last term (n-wise intersection) sign depends on whether n is odd or even for union counting.
- **Incorrect factorial calculations**: For derangements, ensure (n-k)! is computed correctly for each intersection term.

## Revision Tips

1. Practice deriving the formula for Dₙ from inclusion-exclusion to reinforce understanding.
2. Solve at least 3-4 problems each for derangements and onto functions to master the pattern.
3. Create a quick reference card with formulas for different PIE applications.
4. For divisibility problems, always list the divisibility sets and their LCMs systematically.
5. Use the recurrence relation Dₙ = (n-1)(Dₙ₋₁ + Dₙ₋₂) for quick derangement calculations in exams.
