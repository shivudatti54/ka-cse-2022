# Expectation and Variance - Summary

## Key Definitions and Concepts

- **Expected Value E[X]**: The long-run average value of a random variable; for discrete X: E[X] = Σxᵢ·P(X=xᵢ); for continuous X: E[X] = ∫x·f(x)dx

- **Variance Var(X)**: Measures dispersion around the mean; Var(X) = E[(X - μ)²] = E[X²] - (E[X])²

- **Standard Deviation σ(X)**: The square root of variance; √Var(X), in same units as X

- **Covariance Cov(X,Y)**: Measures joint variability; Cov(X,Y) = E[XY] - E[X]E[Y]

## Important Formulas and Theorems

| Concept | Formula |
|---------|---------|
| Linearity of Expectation | E[aX + bY] = aE[X] + bE[Y] |
| Variance Transformation | Var(aX + b) = a²Var(X) |
| Variance of Sum (Independent) | Var(X + Y) = Var(X) + Var(Y) |
| Variance Definition | Var(X) = E[X²] - (E[X])² |
| Chebyshev's Inequality | P(\|X - μ\| ≥ kσ) ≤ 1/k² |
| Law of Total Expectation | E[X] = ΣE[X\|Bᵢ]·P(Bᵢ) |

## Key Points

- Expected value represents the weighted average of all possible outcomes

- Variance is always non-negative; equals zero only for constant random variables

- For independent variables, covariance equals zero (but converse is not always true)

- Standard deviation is more interpretable as it's in original units

- Linearity of expectation holds regardless of independence; variance addition requires independence

- E[X²] is not equal to (E[X])² except in degenerate cases

- Variance measures spread but not direction of deviation from mean

## Common Mistakes to Avoid

1. **Confusing E[X²] with (E[X])²**: These are different—always compute E[X²] separately

2. **Assuming variance formula Var(X + Y) = Var(X) + Var(Y)**: Only true for independent X and Y

3. **Forgetting to square the coefficient**: Var(aX) = a²Var(X), not a·Var(X)

4. **Ignoring absolute convergence**: The expectation sum must converge absolutely for proper definition

## Revision Tips

1. Practice computing expectation and variance from probability distributions—start with simple cases like dice, coins, and cards

2. Memorize the computational formula for variance as it avoids the extra step of finding deviations

3. Work through algorithm analysis examples (linear search, quicksort) to understand practical applications

4. Create a cheat sheet of all formulas and theorems for quick review before exams

5. Solve at least 5-10 problems from each category to build fluency with different problem types