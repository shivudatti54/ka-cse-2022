# Central Limit Theorem - Summary

## Key Definitions

- **Central Limit Theorem**: States that the distribution of sample means approaches a normal distribution as sample size increases, regardless of the population distribution shape
- **Sampling Distribution**: The probability distribution of a statistic (like the sample mean) computed from multiple samples
- **Standard Error (SE)**: The standard deviation of the sampling distribution, equal to σ/√n for the sample mean
- **i.i.d. (Independent and Identically Distributed)**: Random variables that are mutually independent and share the same probability distribution

## Important Formulas

- **Sampling Distribution**: X̄ ~ N(μ, σ²/n)
- **Standard Error**: SE = σ/√n
- **Standardized Z-statistic**: Z = (X̄ - μ) / (σ/√n)
- **Confidence Interval**: μ ± Z_α/2 × (σ/√n)
- **Finite Population Correction**: When sampling without replacement from a finite population, multiply SE by √((N-n)/(N-1))

## Key Points

1. CLT applies regardless of the shape of the original population distribution
2. The sampling distribution of X̄ becomes approximately normal for n ≥ 30 in most cases
3. Larger sample sizes produce smaller standard errors and more precise estimates
4. The theorem requires finite variance; distributions with infinite variance (e.g., Cauchy) are excluded
5. Independence between observations is essential for CLT to hold
6. The convergence to normality is faster for populations closer to normal
7. CLT enables inference about population means even when population distribution is unknown

## Common Mistakes

1. **Confusing population and sampling distributions** - The population may be non-normal, but the sampling distribution of the mean is approximately normal
2. **Using CLT for small samples from highly skewed distributions** - The normal approximation may be poor; n > 50 may be needed
3. **Ignoring the independence requirement** - Dependent samples invalidate CLT applications
4. **Forgetting to divide variance by sample size** - The variance of X̄ is σ²/n, not σ²
5. **Applying CLT when variance is infinite** - Populations like Cauchy distribution violate the finite variance requirement