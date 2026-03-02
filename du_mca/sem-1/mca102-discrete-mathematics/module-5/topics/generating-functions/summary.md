# Generating Functions - Summary

## Key Definitions and Concepts

- **Ordinary Generating Function (OGF)**: For sequence {a₀, a₁, a₂, ...}, G(x) = Σ aₙxⁿ. Used for unlabeled combinatorial structures where order doesn't matter.

- **Exponential Generating Function (EGF)**: E(x) = Σ aₙ(xⁿ/n!). Used for labeled structures where order matters or objects are distinct.

- **Coefficient Extraction**: Denoted [xⁿ]G(x) = aₙ, meaning the coefficient of xⁿ in G(x).

## Important Formulas and Theorems

| Sequence | OGF |
|----------|-----|
| 1, 1, 1, ... | 1/(1-x) |
| 1, 2, 3, ... | 1/(1-x)² |
| C(n+k-1, k-1) | 1/(1-x)ᵏ |
| Fibonacci {Fₙ} | x/(1-x-x²) |
| Catalan {Cₙ} | (1-√(1-4x))/(2x) |

**Operations**:
- Addition: G(x) + H(x) = Σ (aₙ + bₙ)xⁿ
- Multiplication: G(x)H(x) = Σ (Σ aₖbₙ₋ₖ) xⁿ (convolution)
- Shifting: x·G(x) shifts sequence right by one position

## Key Points

1. Generating functions are formal power series—x is a placeholder, not a numerical variable.

2. For recurrence relations: multiply by x⁙, sum over valid n, substitute G(x), solve algebraically, extract coefficients.

3. OGFs are used for combinations (unlabeled objects); EGFs for permutations (labeled objects).

4. The product of generating functions corresponds to selecting from two categories simultaneously (convolution).

5. Partition generating function: ∏(1-xᵏ)⁻¹ counts partitions using parts of all sizes.

6. Partial fraction decomposition is the standard technique for extracting coefficients from rational generating functions.

7. Initial conditions are essential when setting up generating functions for recurrence relations—they determine the unique solution.

## Common Mistakes to Avoid

1. Treating generating functions as functions that accept numerical values (they're formal objects).

2. Forgetting to include all initial conditions when forming the generating function equation for recurrence relations.

3. Using OGF when EGF is required (e.g., for problems involving permutations or distinct labeling).

4. Incorrectly handling the summation index when deriving generating functions from recurrences.

5. Failing to verify that solutions satisfy both the recurrence and initial conditions.

## Revision Tips

1. Practice converting between recurrence relations and their generating function representations.

2. Memorize the 5-6 standard generating functions in the table above—they appear repeatedly.

3. For exam problems, always start by identifying what aₙ represents and what recurrence or combinatorial situation defines it.

4. Work through at least 3-4 complete examples covering different applications (recurrence solving, counting, partitions).

5. When stuck on coefficient extraction, try partial fractions or differentiate known generating functions.