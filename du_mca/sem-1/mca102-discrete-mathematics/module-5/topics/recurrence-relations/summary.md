# Recurrence Relations - Summary

## Key Definitions and Concepts

- **Recurrence Relation:** An equation defining a sequence where each term is expressed in terms of previous terms, together with initial conditions that specify starting values.

- **Order:** The difference between the largest and smallest indices in the recurrence relation; determines the number of roots in the characteristic equation.

- **Linear Recurrence:** A recurrence where each term is a linear combination of previous terms with coefficients that may depend on n but not on the sequence values themselves.

- **Homogeneous vs Non-Homogeneous:** Homogeneous recurrences have f(n) = 0 in the general form; non-homogeneous have a non-zero forcing function.

- **Characteristic Equation:** The polynomial equation rᵏ - c₁rᵏ⁻¹ - ... - cₖ = 0 derived by assuming a solution of the form aₙ = rⁿ.

## Important Formulas and Theorems

- **General Linear Recurrence:** aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ + f(n)

- **Distinct Roots Solution:** aₙ = A₁r₁ⁿ + A₂r₂ⁿ + ... + Aₖrₖⁿ

- **Repeated Roots Solution:** For root r with multiplicity m, include terms (A₁ + A₂n + ... + Aₘnᵐ⁻¹)rⁿ

- **First-Order Linear Solution:** aₙ = cⁿa₀ + d(cⁿ - 1)/(c - 1) for c ≠ 1; aₙ = a₀ + nd for c = 1

- **General Solution Structure:** For non-homogeneous: aₙ = aₙ⁽ʰ⁾ + aₙ⁽ᵖ⁾

## Key Points

- Recurrence relations require both the relation and initial conditions to fully specify a sequence.

- The characteristic equation method works only for linear recurrences with constant coefficients.

- Distinct real roots yield exponential solutions; repeated roots introduce polynomial factors; complex roots yield trigonometric solutions.

- Particular solution guesses depend on the form of f(n): constant→constant, polynomial→polynomial of same degree, exponential→exponential.

- If the particular solution guess overlaps with homogeneous solution terms, multiply by n.

- The Master Theorem provides asymptotic solutions for divide-and-conquer recurrences: T(n) = aT(n/b) + f(n).

- Always verify solutions by substituting back into the original recurrence.

## Common Mistakes to Avoid

1. Forgetting initial conditions—solutions are incomplete without them.

2. Not checking whether guessed particular solution overlaps with homogeneous solution, leading to incorrect particular solution.

3. Solving the characteristic equation incorrectly—always verify roots satisfy the equation.

4. Using the characteristic equation method when coefficients are not constant (use iteration or substitution instead).

5. Not simplifying final answers—expressions like 2(3)ⁿ should be written clearly.

## Revision Tips

1. Practice forming recurrence relations from word problems before solving them.

2. Memorize the particular solution guess table for common f(n) forms.

3. Work through at least 5-10 varied problems covering homogeneous, non-homogeneous, and application-based scenarios.

4. Focus on verification steps—examiners often check if students verify their solutions.

5. Review algorithm analysis examples to connect theoretical concepts with practical computing applications.