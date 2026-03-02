# Testing Of Hypothesis - Summary

## Key Definitions

- **Null Hypothesis (H₀)**: The hypothesis of no effect or no difference; represents the status quo or default assumption that we attempt to disprove.

- **Alternative Hypothesis (H₁)**: The claim or hypothesis we want to establish; represents the effect or difference we suspect exists.

- **Type I Error**: Rejecting H₀ when it is actually true (false positive); probability = α (level of significance).

- **Type II Error**: Failing to reject H₀ when it is actually false (false negative); probability = β.

- **Power of Test**: Probability of correctly rejecting a false H₀, equal to 1 - β.

- **Test Statistic**: A standardized value computed from sample data used to make decisions about H₀.

- **Critical Region**: The set of values for which we reject H₀; determined by α.

- **P-value**: Smallest level of significance at which H₀ can be rejected; probability of obtaining a result as extreme as observed assuming H₀ is true.

## Important Formulas

- **Z-test for population mean (σ known)**: $Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$

- **Z-test for population mean (σ unknown, large sample)**: $Z = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$

- **Z-test for population proportion**: $Z = \frac{\hat{p} - p_0}{\sqrt{p_0(1-p_0)/n}}$

- **Two-sample Z-test for difference of means**: $Z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$

- **Critical values**: Z₀.₀₅ = ±1.96 (two-tailed), Z₀.₀₅ = 1.645 (right-tailed), Z₀.₀₅ = -1.645 (left-tailed) at α = 0.05

## Key Points

1. Hypothesis testing is a decision-making procedure based on sample evidence about population parameters.

2. The null hypothesis is assumed true until sufficient evidence suggests otherwise; the burden of proof lies with the alternative hypothesis.

3. A smaller α (significance level) makes it harder to reject H₀ but increases Type II error risk.

4. One-tailed tests are more powerful for detecting effects in a specific direction but should only be used when that direction is theoretically justified.

5. The p-value provides more information than binary reject/fail-to-reject decisions; it indicates the strength of evidence against H₀.

6. Statistical significance does not imply practical significance; always consider effect size and context.

7. Large sample tests (Z-tests) require n ≥ 30 or known population parameters for validity.

8. For proportions, the conditions np ≥ 5 and n(1-p) ≥ 5 must be satisfied for valid Z-test.

## Common Mistakes

1. **Confusing the alternative hypothesis with the null hypothesis** - Always remember H₀ contains the equality (=, ≥, ≤) while H₁ contains the inequality (≠, >, <).

2. **Using one-tailed test when two-tailed is appropriate** - Using a one-tailed test when the alternative simply states "different" is a common error.

3. **Ignoring assumptions** - Applying Z-test without checking sample size or population standard deviation conditions.

4. **Interpreting "fail to reject" as "prove true"** - Failing to reject H₀ means insufficient evidence, not that H₀ is definitely true.

5. **Confusing p-value with probability of hypothesis** - The p-value is P(data|H₀ is true), not P(H₀ is true|data).