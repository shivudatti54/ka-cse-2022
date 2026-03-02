# Test of Significance for Means of Two Small Samples

=============================================

## Definitions and Notations

- **Null Hypothesis (H0)**: The population mean difference is zero (μ1 - μ2 = 0)
- **Alternative Hypothesis (H1)**: The population mean difference is not zero (μ1 - μ2 ≠ 0)
- **Sample Size**: n1 and n2 for two independent samples
- **Sample Means**: x̄1 and x̄2 for two independent samples
- **Population Variance**: σ1^2 and σ2^2 for two independent populations

## Formulas and Theorems

- **Sampling Distribution of the Difference**: (x̄1 - x̄2) ~ N(μ1 - μ2, σ1^2/n1 + σ2^2/n2)
- **Test Statistic**: t = (x̄1 - x̄2) / sqrt((σ1^2/n1 + σ2^2/n2))
- **Critical Region**: t > t*(α, n1 + n2 - 2) or t < -t*(α, n1 + n2 - 2)
- **T-Test Statistic**: t = (x̄1 - x̄2) / sqrt((σ1^2/n1 + σ2^2/n2))
- **T-Test Formula**: t = (x̄1 - x̄2) / sqrt((σ1^2/n1 + σ2^2/n2)) ≈ z = (x̄1 - x̄2) / sqrt((σ1^2/n1 + σ2^2/n2)) for large samples

## Important Concepts

- **Assumptions**:
  - Independence of samples
  - Normality of samples
  - Equal variances (homoscedasticity)
- **Interpretation**:
  - If the test statistic falls within the critical region, reject H0 and conclude that the means are significantly different
  - Otherwise, fail to reject H0 and conclude that the means are not significantly different

## Common Errors

- **Type I Error**: Rejecting H0 when it is true
- **Type II Error**: Failing to reject H0 when it is false
