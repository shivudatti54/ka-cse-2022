# Student's t-Distribution - Summary

## Key Definitions and Concepts

- STUDENT'S T-DISTRIBUTION: A probability distribution used for estimating population means when sample sizes are small and population standard deviation is unknown. Named William Sealy Gosset ("Student").

- DEGREES OF FREEDOM (ν): The parameter that defines the t-distribution. For a sample of size n, df = n - 1. Higher df values make the distribution approach the normal distribution.

- T-STATISTIC: A test statistic computed as t = (x̄ - μ) / (s/√n) that follows the t-distribution under the null hypothesis.

## Important Formulas and Theorems

- ONE-SAMPLE T-TEST: t = (x̄ - μ₀) / (s/√n) with df = n - 1

- TWO-SAMPLE INDEPENDENT T-TEST (equal variances): t = (x̄₁ - x̄₂) / (sp√(1/n₁ + 1/n₂)) with df = n₁ + n₂ - 2

- POOLED VARIANCE: sp² = ((n₁-1)s₁² + (n₂-1)s₂²) / (n₁ + n₂ - 2)

- CONFIDENCE INTERVAL FOR MEAN: x̄ ± t(α/2, n-1) × (s/√n)

- CENTRAL LIMIT THEOREM FOR T: As df → ∞, t-distribution approaches N(0,1)

## Key Points

- The t-distribution has HEAVIER TAILS than the normal distribution, accounting for increased uncertainty when σ is estimated from data

- The distribution is SYMMETRIC around zero with mean = median = mode = 0

- Variance exists only for df > 2, equaling df/(df - 2)

- For practical purposes, t-distribution approximates normal distribution when n ≥ 30 or df ≥ 30

- Three main t-tests: one-sample, two-sample independent, and paired samples

- Always check normality assumption before applying t-tests; consider non-parametric alternatives for non-normal data

- The t-test is ROBUST to moderate violations of normality, especially with larger sample sizes

## Common Mistakes to Avoid

- CONFUSING Z AND T: Using z instead of t when σ is unknown, even for small samples

- FORGETTING DEGREES OF FREEDOM: Always subtract 1 (or 2 for two-sample tests) when determining df

- USING ONE-TAILED CRITICAL VALUES FOR TWO-TAILED TESTS: The test type must match the alternative hypothesis

- IGNORING EQUAL VARIANCE ASSUMPTION: In two-sample tests, verify whether equal variances can be assumed or use Welch's correction

- MISINTERPRETING P-VALUES: Remember that p-value depends on the direction of the alternative hypothesis

## Revision Tips

- MEMORIZE THE DEGREES OF FREEDOM FORMULAS: n-1 for one sample, n₁ + n₂ - 2 for two independent samples with equal variances, n-1 for paired samples

- PRACTICE READING T-TABLES: Most DU exams provide simplified t-tables; learn to extract critical values quickly

- WORK THROUGH AT LEAST THREE PROBLEMS OF EACH TYPE: One-sample, two-sample, and paired t-tests

- UNDERSTAND THE INTUITION: Heavy tails = more uncertainty = wider confidence intervals = harder to reject null hypothesis

- KNOW WHEN TO USE T VS NORMAL: t for unknown σ, small n; normal for known σ or large n