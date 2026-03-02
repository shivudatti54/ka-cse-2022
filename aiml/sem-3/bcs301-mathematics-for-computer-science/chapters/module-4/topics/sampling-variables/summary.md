# Sampling Variables - Summary

## Key Definitions and Concepts

- **Population**: The complete set of all observations about which conclusions are to be drawn; characterized by parameters (μ, σ, P).
- **Sample**: A subset of the population selected for study; characterized by statistics (x̄, s, p̂).
- **Sampling Distribution**: The probability distribution of a statistic computed from repeated samples of size n.
- **Standard Error (SE)**: The standard deviation of a sampling distribution; measures variability of a statistic across samples.
- **Unbiased Estimator**: A statistic whose expected value equals the population parameter it estimates.

## Important Formulas and Theorems

- **Sample Mean**: x̄ = Σxi / n
- **Sample Variance**: s² = Σ(xi - x̄)² / (n - 1)
- **Standard Error of Mean (infinite population)**: SE(x̄) = σ / √n
- **Standard Error (finite population without replacement)**: SE(x̄) = (σ/√n) × √[(N-n)/(N-1)]
- **Expected Value of Sample Mean**: E(x̄) = μ
- **Expected Value of Sample Variance**: E(s²) = σ²
- **Law of Large Numbers**: Sample mean converges to population mean as n → ∞

## Key Points

- Sample statistics are random variables with their own probability distributions called sampling distributions.
- The sample mean is an UNBIASED estimator of the population mean—the expected value equals the population parameter.
- Standard error decreases as sample size increases, but at a rate proportional to the square root of n.
- To reduce standard error by half, sample size must be quadrupled.
- The finite population correction factor should only be applied when sampling without replacement from a finite population.
- The sampling distribution of the sample mean has the same mean as the population but smaller standard deviation.
- The sample variance uses n-1 (not n) in the denominator to ensure unbiasedness.
- Different samples yield different values of statistics—this variability is quantified by the sampling distribution.

## Common Mistakes to Avoid

- Confusing population parameters with sample statistics (using wrong notation).
- Using n instead of (n-1) in the sample variance formula—this produces a biased estimate.
- Applying the finite population correction factor when sampling with replacement (correction is not needed).
- Forgetting that the standard error measures the variability of the statistic, not individual observations.
- Assuming the sampling distribution has the same shape as the population distribution—they are generally different.

## Revision Tips

- Practice computing sample statistics from raw data sets until the formulas become automatic.
- Memorize the standard error formula and understand each component—σ represents population variability, √n represents the reduction from averaging n observations.
- Create a comparison table of population vs. sample characteristics (notation, what they describe, typical values).
- Solve problems involving different sample sizes to internalize the square root relationship.
- Review the connection between this topic and the Central Limit Theorem—it forms the foundation for inference procedures.