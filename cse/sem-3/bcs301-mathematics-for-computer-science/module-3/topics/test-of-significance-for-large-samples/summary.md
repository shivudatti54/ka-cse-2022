# Test Of Significance For Large Samples - Summary

## Key Definitions
- **Null Hypothesis (H₀)**: The hypothesis of no effect or no difference, serving as the default assumption to be tested
- **Alternative Hypothesis (H₁)**: The competing hypothesis that contradicts H₀ and represents the research claim
- **Test Statistic**: A numerical measure computed from sample data that is used to determine whether to reject H₀
- **Significance Level (α)**: The probability of committing a Type I error, typically set at 0.05 or 0.01
- **P-value**: The probability of obtaining test results at least as extreme as observed, assuming H₀ is true

## Important Formulas
- **Test for single mean (large sample)**: z = (x̄ - μ₀) / (s/√n)
- **Test for single proportion**: z = (p̂ - p₀) / √[p₀(1-p₀)/n]
- **Test for difference of two means**: z = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)
- **Test for difference of two proportions**: z = (p̂₁ - p̂₂) / √[p̄(1-p̄)(1/n₁ + 1/n₂)]

## Key Points
1. Large sample tests (n ≥ 30) utilize the standard normal distribution due to the Central Limit Theorem
2. The choice between one-tailed and two-tailed tests must be made before collecting data based on the research hypothesis
3. A p-value less than α leads to rejection of H₀; larger p-values fail to provide evidence against H₀
4. Type I error (α) and Type II error (β) have an inverse relationship—increasing one decreases the other
5. For two-sample tests, samples must be independent unless using paired comparison methods
6. The sample standard deviation (s) can substitute for population σ in large samples
7. Statistical significance does not imply practical significance—effect size should also be considered

## Common Mistakes
1. Using t-tests instead of z-tests for large samples (unnecessary when n ≥ 30)
2. Changing from two-tailed to one-tailed tests after observing data direction (data snooping)
3. Confusing p-value with the probability that H₀ is true
4. Interpreting "fail to reject H₀" as proof that H₀ is true
5. Ignoring assumptions such as sample independence and random sampling
6. Using small sample formulas for large samples or vice versa