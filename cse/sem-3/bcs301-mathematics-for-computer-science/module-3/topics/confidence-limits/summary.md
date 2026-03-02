# Confidence Limits - Summary

## Key Definitions

- **Confidence Interval:** An interval estimate for a population parameter that provides a range of values within which the parameter is likely to fall with a specified probability (confidence level).

- **Confidence Limits:** The lower and upper endpoints of a confidence interval.

- **Confidence Level (1-α):** The probability that the method used to construct the interval will produce an interval containing the true parameter in repeated sampling.

- **Margin of Error:** The maximum expected difference between the point estimate and the true parameter, equal to the critical value multiplied by the standard error.

- **Critical Value:** The value from the sampling distribution (z or t) that corresponds to the desired confidence level.

## Important Formulas

- **Large Sample Mean (σ unknown):** x̄ ± zₐ/₂ × (s/√n)

- **Small Sample Mean (σ unknown):** x̄ ± tₐ/₂,n-1 × (s/√n)

- **Proportion:** p̂ ± zₐ/₂ × √[p̂(1-p̂)/n]

- **Margin of Error:** zₐ/₂ × (s/√n) for means

- **Sample Size for Desired Margin of Error:** n = (zₐ/₂ × σ/E)² where E is desired margin of error

## Key Points

1. A 95% confidence interval means that if we repeat the sampling 100 times, approximately 95 intervals will contain the true parameter.

2. For large samples (n ≥ 30), use the z-distribution regardless of population normality due to the Central Limit Theorem.

3. For small samples (n < 30) from normal populations, use the t-distribution with (n-1) degrees of freedom.

4. The t-distribution has heavier tails than the normal distribution, accounting for additional uncertainty in small samples.

5. Higher confidence levels produce wider intervals; lower confidence levels produce narrower intervals.

6. The width of a confidence interval is inversely proportional to √n; quadrupling sample size halves the interval width.

7. For proportions, the normal approximation is valid when np̂ ≥ 5 and n(1-p̂) ≥ 5.

8. Confidence intervals provide more information than point estimates as they indicate precision of the estimate.

## Common Mistakes

1. **Incorrect interpretation:** Saying "there is a 95% probability the parameter is in the interval" is wrong—either it is or it isn't for a fixed interval.

2. **Using z for small samples:** Always use t-distribution when σ is unknown and n < 30, even if the sample data appears normal.

3. **Ignoring conditions:** Failing to check the conditions for using normal approximation for proportions (np̂ ≥ 5, n(1-p̂) ≥ 5).

4. **Confusing confidence level with probability:** The confidence level applies to the method, not to any particular interval after it is computed.