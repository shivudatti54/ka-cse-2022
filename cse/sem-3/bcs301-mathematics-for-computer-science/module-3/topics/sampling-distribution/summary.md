# Sampling Distribution - Summary

## Key Definitions

- **Sampling Distribution**: The probability distribution of a statistic (e.g., sample mean) computed from all possible samples of a given size drawn from a population.

- **Standard Error (SE)**: The standard deviation of a sampling distribution, measuring the variability of the sample statistic from sample to sample.

- **Central Limit Theorem (CLT)**: The theorem stating that the sampling distribution of the sample mean approaches a normal distribution as sample size increases, regardless of the population's distribution.

- **Point Estimate**: A single value estimate of a population parameter computed from sample data.

- **Bias**: The difference between the expected value of a statistic and the true population parameter it estimates.

## Important Formulas

- **Standard Error of Mean**: SE(x̄) = σ/√n (known σ) or SE(x̄) = s/√n (estimated σ)

- **Standard Error of Proportion**: SE(p̂) = √[P(1-P)/n]

- **Mean of Sampling Distribution**: E(x̄) = μ, E(p̂) = P

- **Variance of Sampling Distribution**: Var(x̄) = σ²/n, Var(p̂) = P(1-P)/n

- **Sample Size for Mean**: n = (z* × σ / E)²

- **Sample Size for Proportion**: n = (z*)² × P(1-P) / E²

## Key Points

1. Sampling distributions provide the theoretical foundation for all inferential statistics by describing how statistics vary across samples.

2. The standard error decreases with the square root of sample size, meaning quadrupling the sample size halves the standard error.

3. The Central Limit Theorem allows us to use normal distribution methods even when the population distribution is unknown or non-normal.

4. For proportions, the normal approximation to the sampling distribution is valid when np ≥ 5 and n(1-P) ≥ 5.

5. The t-distribution should be used instead of the normal distribution when the population standard deviation is unknown and estimated from the sample.

6. As sample size increases, the sampling distribution becomes more concentrated around the population parameter, leading to more precise estimates.

7. The chi-square distribution is used for variance-related inferences and has degrees of freedom parameter that affects its shape.

## Common Mistakes

1. **Confusing population standard deviation with standard error**: The population standard deviation (σ) measures variability in the population, while standard error measures variability in the sampling distribution.

2. **Using normal distribution when t-distribution is appropriate**: When σ is unknown and estimated by s, always use t-distribution for small samples (n < 30).

3. **Forgetting to check conditions**: Always verify that requirements for normal approximation (like np ≥ 5 for proportions) are met before applying the formulas.

4. **Incorrectly interpreting confidence intervals**: A 95% confidence interval does not mean there is a 95% probability the parameter lies in the interval; it means that if we repeated sampling many times, 95% of such intervals would contain the true parameter.

5. **Using sample standard deviation formula for population**: Remember that the sample variance formula uses (n-1) in the denominator (Bessel's correction), not n, to provide an unbiased estimate of population variance.