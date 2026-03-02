# Student's t-Distribution - Summary

## Key Definitions and Concepts

- Student's t-distribution: A probability distribution used for estimating population mean when sample size is small and population standard deviation is unknown. It was discovered by William Sealy Gosset (published as "Student").

- Degrees of freedom (ν): The parameter that determines the shape of t-distribution. For a sample of size n, df = n-1. It represents the number of independent observations available for estimating variability.

- t-statistic: The test statistic that follows t-distribution under null hypothesis, calculated as t = (X̄ - μ₀)/(s/√n) for one-sample tests.

## Important Formulas and Theorems

- One-sample t-test statistic: t = (X̄ - μ₀)/(s/√n) with df = n-1

- Two-sample t-test (equal variances): t = (X̄₁ - X̄₂)/[sₚ × √(1/n₁ + 1/n₂)] with df = n₁ + n₂ - 2, where sₚ is the pooled standard deviation

- Two-sample t-test (unequal variances - Welch's): Similar formula but using individual standard deviations with adjusted degrees of freedom

- Paired t-test: t = d̄/(s_d/√n) with df = n-1, where d̄ is mean of differences

- Confidence interval for μ: X̄ ± t(α/2, n-1) × (s/√n)

- Relationship: As ν → ∞, t → N(0,1). Also, t² with ν df follows F(1, ν) distribution.

## Key Points

- The t-distribution has heavier tails than the normal distribution, accounting for additional uncertainty when σ is estimated from sample data.

- For n > 30, t-distribution closely approximates the standard normal distribution.

- Always use t-test when population standard deviation is unknown (which is the typical case).

- The t-test assumes that the population from which samples are drawn is approximately normally distributed.

- For paired designs, compute differences first, then apply one-sample t-test to these differences.

- In two-sample tests, check for equal variances assumption before selecting pooled or Welch's t-test.

- The t-distribution is symmetric about zero, so t(α, df) = -t(1-α, df).

## Common Mistakes to Avoid

- Using z-test when population standard deviation is unknown instead of t-test.

- Confusing degrees of freedom with sample size (remember df = n-1, not n).

- Using two-sample t-test for paired data instead of paired t-test.

- Forgetting to specify the degrees of freedom when looking up critical t-values.

- Not checking the normality assumption for small samples (n < 30).

## Revision Tips

- Practice computing t-statistics with different sample sizes and understanding how df changes.

- Memorize the relationship between t and normal distribution (convergence as df increases).

- Solve at least 3-4 problems covering one-sample, two-sample, and paired t-tests.

- Remember the key property: heavier tails → larger critical values → wider confidence intervals compared to normal approximation.

- Understand the logic: estimating σ introduces uncertainty, t-distribution accounts for this by having wider tails than normal.