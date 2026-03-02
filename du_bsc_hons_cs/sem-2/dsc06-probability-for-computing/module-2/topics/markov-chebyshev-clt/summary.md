# Markov's Inequality, Chebyshev's Inequality, and Central Limit Theorem - Summary

## Key Definitions and Concepts

- **Markov's Inequality:** For a non-negative random variable X with E(X) = μ, P(X ≥ a) ≤ μ/a for a > 0. Requires only the mean.

- **Chebyshev's Inequality:** For a random variable X with mean μ and variance σ², P(|X - μ| ≥ kσ) ≤ 1/k² for k > 0. Requires mean and variance.

- **Weak Law of Large Numbers:** Sample mean X̄ₙ converges in probability to true mean μ as n → ∞; proved using Chebyshev's Inequality.

- **Central Limit Theorem:** For i.i.d. variables with finite variance, the standardized sample mean converges to N(0,1), meaning X̄ₙ ≈ N(μ, σ²/n) for large n.

## Important Formulas and Theorems

| Theorem | Formula | Conditions |
|---------|---------|------------|
| Markov | P(X ≥ a) ≤ E(X)/a | X ≥ 0, a > 0 |
| Chebyshev | P(\|X - μ\| ≥ kσ) ≤ 1/k² | Finite μ, σ² |
| CLT | X̄ₙ ~ N(μ, σ²/n) | n ≥ 30, i.i.d., finite σ² |

## Key Points

- Markov's Inequality is universally applicable but often provides loose bounds.
- Chebyshev's Inequality always gives tighter bounds than Markov when variance is known.
- The CLT explains why normal distribution appears everywhere—it is the "attractor" for sums of random variables.
- Standard error = σ/√n decreases as sample size increases.
- For CLT: always standardize using Z = (X̄ - μ)/(σ/√n).
- WLLN guarantees convergence of sample mean to population mean in probability.
- These inequalities are essential for analyzing randomized algorithms and bounding errors in computing.

## Common Mistakes to Avoid

1. **Forgetting to check conditions:** Applying Markov to variables that can be negative, or CLT when n is too small.
2. **Confusing variance of sample mean:** Using σ² instead of σ²/n for Var(X̄ₙ).
3. **Standardization errors:** Using wrong formula or forgetting to divide by standard error (σ/√n).
4. **Misinterpreting inequality direction:** These give upper bounds, not exact probabilities.

## Revision Tips

1. Practice 2-3 problems from each inequality type before the exam.
2. Memorize the exact forms of all three theorems with their conditions.
3. Remember: Markov → Mean only; Chebyshev → Mean + Variance; CLT → Approximation to Normal.
4. For CLT problems, always verify n ≥ 30 before applying the approximation.
5. Review the relationship: Chebyshev → WLLN → foundation for statistical inference.