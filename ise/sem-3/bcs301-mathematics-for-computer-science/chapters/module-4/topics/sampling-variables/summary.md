# Sampling Variables - Summary

## Key Definitions and Concepts

- POPULATION: Complete set of all observations; characterized by parameters (μ, σ²)
- SAMPLE: Subset of population selected for study; characterized by statistics (X̄, S²)
- SAMPLING VARIABLE: A random variable derived from sample observations
- SAMPLING DISTRIBUTION: Probability distribution of a sample statistic
- STANDARD ERROR: Standard deviation of a sampling distribution (measure of precision)

## Important Formulas and Theorems

- Sample Mean: X̄ = ΣXᵢ/n
- Expected Value of Sample Mean: E(X̄) = μ (unbiased estimator)
- Variance of Sample Mean: Var(X̄) = σ²/n (with replacement) or Var(X̄) = (σ²/n)[(N-n)/(N-1)] (without replacement)
- Sample Variance: S² = Σ(Xᵢ - X̄)²/(n-1)
- Expected Value of Sample Variance: E(S²) = σ² (unbiased estimator)
- Standard Error: SE(X̄) = σ/√n
- Sampling Distribution: If population ~ N(μ, σ²), then X̄ ~ N(μ, σ²/n)
- Chi-Square Relation: (n-1)S²/σ² ~ χ²ₙ₋₁

## Key Points

- Sample statistics (X̄, S²) are random variables with their own probability distributions
- The sample mean is an UNBIASED ESTIMATOR of population mean: E(X̄) = μ
- The sample variance is an UNBIASED ESTIMATOR of population variance: E(S²) = σ²
- The factor (n-1) in sample variance provides unbiasedness; (n-1) represents DEGREES OF FREEDOM
- For normal populations, X̄ and S² are INDEPENDENT random variables
- The standard error decreases as √n— quadrupling sample size halves the standard error
- Sampling distribution of X̄ is narrower (less variable) than the population distribution
- The Finite Population Correction factor √[(N-n)/(N-1)] applies when sampling without replacement

## Common Mistakes to Avoid

- Confusing population standard deviation (σ) with standard error (σ/√n)—they are different measures
- Using n instead of (n-1) in the sample variance formula—this produces a biased estimator
- Forgetting the Finite Population Correction when sampling without replacement from small populations
- Assuming X̄ equals μ—the sample mean varies around μ with variance σ²/n
- Conflating the population distribution with the sampling distribution

## Revision Tips

- Practice computing sample mean and variance from raw data repeatedly
- Memorize the key expected value results: E(X̄) = μ and E(S²) = σ²
- Understand intuitively why the sampling distribution is narrower than the population distribution
- Work through problems involving probability calculations using the sampling distribution of X̄
- Review the derivation of why (n-1) provides unbiasedness—this reinforces conceptual understanding