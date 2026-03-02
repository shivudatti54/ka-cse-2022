# Comparison of Large Samples - Summary

## Key Definitions
- **Large Sample**: A sample with size n ≥ 30, permitting the use of normal distribution approximations.
- **Independent Samples**: Two samples drawn from different populations where the selection of one does not influence the selection of the other.
- **Paired Samples**: Samples where observations are matched or made on the same subjects (e.g., before-after measurements).
- **Pooled Variance**: The combined estimate of common population variance when assuming equal variances.
- **Two-Tailed Test**: A test where the alternative hypothesis states the parameters are not equal (≠).
- **One-Tailed Test**: A test where the alternative hypothesis specifies direction (< or >).

## Important Formulas
- **Z-test for difference of means**: Z = (X̄₁ - X̄₂) / √(s₁²/n₁ + s₂²/n₂)
- **Z-test for difference of proportions**: Z = (p̂₁ - p̂₂) / √(p̂(1-p̂)(1/n₁ + 1/n₂))
- **Pooled variance**: s²p = ((n₁-1)s₁² + (n₂-1)s₂²) / (n₁ + n₂ - 2)
- **Confidence interval for μ₁ - μ₂**: (X̄₁ - X̄₂) ± Zα/2 × √(s₁²/n₁ + s₂²/n₂)
- **Paired test Z-statistic**: Z = d̄ / (s_d/√n)

## Key Points
- Large sample theory relies on the Central Limit Theorem, which states that sample means approach normal distribution as sample size increases.
- The choice between one-tailed and two-tailed tests depends on the research hypothesis about the direction of difference.
- Failing to reject H₀ does not prove H₀ is true; it only indicates insufficient evidence against it.
- For proportions, the pooled estimate under H₀ should always be used in the standard error calculation.
- The significance level (α) determines the critical values and hence the rejection region.
- Type I error (rejecting true H₀) and Type II error (failing to reject false H₀) are inversely related.
- Practical significance should be considered alongside statistical significance.

## Common Mistakes
1. **Using sample standard deviations incorrectly**: For proportions, always use the pooled proportion under H₀ in the denominator, not the individual sample proportions.

2. **Ignoring the independence assumption**: Applying two-sample tests to dependent data leads to invalid conclusions.

3. **Confusing statistical and practical significance**: A statistically significant result may have no practical importance if the effect size is tiny.

4. **Incorrectly pooling variances**: Pooled variance should only be used when we assume equal population variances; otherwise, use separate variance estimates.

5. **One-tailed vs. two-tailed confusion**: Using a one-tailed test when a two-tailed test is appropriate (or vice versa) can lead to incorrect conclusions about the direction of significance.