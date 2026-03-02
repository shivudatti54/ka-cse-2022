# Student's T Distribution - Summary

## Key Definitions

- **Student's t-distribution**: A probability distribution used estimating population means when for sample sizes are small and population standard deviation is unknown.

- **Degrees of freedom (ν)**: The parameter that defines the shape of the t-distribution; for a sample of size n, ν = n - 1.

- **Critical value (t_{α,ν})**: The value such that the probability to the right equals α for a given significance level and degrees of freedom.

## Important Formulas

- **Probability Density Function**:
$$f(t) = \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\Gamma\left(\frac{\nu}{2}\right)}\left(1+\frac{t^2}{\nu}\right)^{-\frac{\nu+1}{2}}$$

- **Test Statistic for One-Sample T-Test**:
$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$$

- **Confidence Interval Margin of Error**:
$$E = t_{\alpha/2, \nu} \times \frac{s}{\sqrt{n}}$$

- **Relationship to Normal and Chi-Square**:
$$T = \frac{Z}{\sqrt{X^2/\nu}}$$

## Key Points

1. The t-distribution is symmetric about zero, just like the standard normal distribution.

2. It has heavier tails than the normal distribution, accounting for increased uncertainty in small samples.

3. As degrees of freedom increase, the t-distribution approaches the standard normal distribution.

4. For hypothesis testing with unknown population standard deviation and n < 30, always use the t-distribution.

5. The t-test assumes the population from which the sample is drawn is approximately normally distributed.

6. For a one-sample t-test, degrees of freedom = n - 1.

7. Two-tailed tests split α between both tails; one-tailed tests place all α in one tail.

8. The t-distribution was developed by William Sealy Gosset (pseudonym "Student") in 1908.

## Common Mistakes

1. **Using z instead of t**: Applying the normal distribution when the population standard deviation is unknown and the sample is small (n < 30), leading to overly narrow confidence intervals and increased Type I error.

2. **Incorrect degrees of freedom**: Forgetting to subtract 1 from sample size (n - 1) when determining degrees of freedom, which produces incorrect critical values.

3. **Ignoring normality assumption**: Applying t-tests without verifying that the underlying population is approximately normal, which can produce invalid results especially with very small samples.

4. **Misreading t-tables**: Confusing one-tailed and two-tailed values; a two-tailed α of 0.05 corresponds to t₀.₀₂₅ in the table, not t₀.₀₅.