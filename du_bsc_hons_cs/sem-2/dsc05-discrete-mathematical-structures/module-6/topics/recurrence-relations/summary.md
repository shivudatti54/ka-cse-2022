# Recurrence Relations - Summary

## Key Definitions and Concepts

- **Recurrence Relation**: An equation defining a sequence recursively, expressing aₙ as a function of preceding terms aₙ₋₁, aₙ₋₂, ..., aₙ₋ₖ
- **Order**: Number of preceding terms needed (k in aₙ depends on aₙ₋₁ through aₙ₋ₖ)
- **Initial Conditions**: Base values (typically a₀ through aₖ₋₁) needed to compute the sequence
- **Linear Recurrence**: Each term is a linear combination of previous terms
- **Homogeneous Recurrence**: The non-recursive part f(n) equals zero
- **Characteristic Equation**: For aₙ = c₁aₙ₋₁ + ... + cₖaₙ₋ₖ, the equation is rᵏ - c₁rᵏ⁻¹ - ... - cₖ = 0

## Important Formulas and Theorems

- **Homogeneous Solution**: For distinct roots r₁, r₂, ..., rₖ: aₙ^(h) = A₁r₁ⁿ + A₂r₂ⁿ + ... + Aₖrᵏⁿ
- **Repeated Roots**: If r₁ has multiplicity m, include terms (A₁ + A₂n + ... + Aₘnᵐ⁻¹)r₁ⁿ
- **General Solution**: aₙ = aₙ^(h) + aₙ^(p), where aₙ^(p) is any particular solution
- **Master Theorem**: For T(n) = aT(n/b) + f(n):
  - If f(n) = O(n^logₐᵇ - ε): T(n) = Θ(n^logₐᵇ)
  - If f(n) = Θ(n^logₐᵇ): T(n) = Θ(n^logₐᵇ log n)
  - If f(n) = Ω(n^logₐᵇ + ε): T(n) = Θ(f(n))

## Key Points

- Recurrence relations are essential for algorithm complexity analysis
- Fibonacci sequence (Fₙ = Fₙ₋₁ + Fₙ₋₂) is a classic example of second-order homogeneous recurrence
- The characteristic equation method solves linear recurrences with constant coefficients systematically
- Particular solution form depends on f(n): polynomial → polynomial guess; bⁿ → bⁿ guess
- Master Theorem provides quick complexity analysis for divide-and-conquer recurrences
- Common algorithm recurrences: Binary Search T(n)=T(n/2)+Θ(1)→Θ(log n); Merge Sort T(n)=2T(n/2)+Θ(n)→Θ(n log n)

## Common Mistakes to Avoid

- Forgetting to use initial conditions when solving for constants in the general solution
- Choosing the wrong form for particular solution when f(n) overlaps with homogeneous solution
- Incorrectly applying Master Theorem when f(n) is polynomial but not polynomially smaller/larger
- Not verifying the final solution by substituting back into the original recurrence

## Revision Tips

1. Practice solving at least 5 homogeneous and 5 non-homogeneous recurrence relations from past DU papers
2. Memorize the Master Theorem cases with the three boundary conditions (less than, equal to, greater than n^logₐᵇ)
3. For quick recall: remember that Fibonacci gives exponential, binary search gives logarithmic, merge sort gives n log n
4. Always write the characteristic equation first when dealing with linear constant-coefficient recurrences