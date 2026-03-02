# Test of Significance for Small Samples - Summary

## Key Definitions

- **Student's t-distribution**: A probability distribution used for small sample inference when population variance is unknown, with heavier tails than the normal distribution and shape determined by degrees of freedom.

- **Degrees of freedom (df)**: A parameter that determines the shape of the t-distribution; for a sample of size n, df = n - 1.

- **Small sample test**: Statistical test applicable when sample size is less than 30, requiring the use of t-distribution rather than normal distribution.

- **Paired observations**: Related measurements taken on the same subject or under similar conditions, allowing for more powerful comparison by controlling for inter-subject variability.

- **Pooled variance**: Combined estimate of common population variance when assuming equal variances in two-sample t-test.

## Important Formulas

- **One-sample t-statistic**: $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ with df = n - 1

- **Two-sample t-statistic (pooled)**: $t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{1/n_1 + 1/n_2}}$ with df = n₁ + n₂ - 2

- **Pooled standard deviation**: $s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}$

- **Chi-square statistic**: $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$ with df = k - 1

## Key Points

1. Small sample tests use t-distribution instead of normal distribution because the latter underestimates variability when population variance is estimated from limited data.

2. As degrees of freedom increase, t-distribution converges to standard normal distribution; for df > 30, the difference is negligible.

3. The one-sample t-test compares a sample mean to a known population value, useful for benchmarking algorithm performance.

4. Two-sample t-test compares means from two independent groups, with Welch's test preferred when variances cannot be assumed equal.

5. Paired t-test is more powerful than two-sample t-test when observations are naturally paired, as it removes between-subject variation.

6. Chi-square test requires expected frequencies of at least 5 in each cell; otherwise, results may be unreliable.

7. All small sample parametric tests assume the underlying population follows a normal distribution.

8. P-values in small sample tests are more extreme than in large sample tests for the same effect size, reflecting greater uncertainty.

## Common Mistakes

1. **Using z-test instead of t-test**: Applying large sample methods to small samples without considering the increased uncertainty leads to incorrect conclusions.

2. **Ignoring the normality assumption**: Failing to check whether data approximately follows a normal distribution invalidates small sample test results.

3. **Not pooling when appropriate**: Using Welch's t-test when equal variances can be assumed reduces statistical power unnecessarily.

4. **Forgetting degrees of freedom**: Using the wrong degrees of freedom when looking up critical values produces incorrect decision boundaries.

5. **Misinterpreting paired vs. independent design**: Treating paired data as independent samples inflates Type I error rates and produces incorrect conclusions.