# Test Of Significances - Summary

## Key Definitions

- **Test of Significance**: A statistical procedure for making decisions about population parameters based on sample data.

- **Null Hypothesis (H₀)**: The default assumption that there is no significant difference or effect in the population; the hypothesis we attempt to reject.

- **Alternative Hypothesis (H₁)**: The claim that there is a significant difference or effect; the hypothesis we seek evidence for.

- **Type I Error (α)**: Rejecting the null hypothesis when it is actually true; also known as a false positive.

- **Type II Error (β)**: Failing to reject the null hypothesis when it is actually false; also known as a false negative.

- **Significance Level (α)**: The probability of committing a Type I error; typically set at 0.05, 0.01, or 0.10.

- **Test Statistic**: A standardized value computed from sample data that measures deviation from the null hypothesis.

- **P-value**: The probability of obtaining results at least as extreme as observed, assuming H₀ is true.

## Important Formulas

- **One-sample z-test for mean**: z = (x̄ - μ₀) / (σ/√n)

- **One-sample z-test (with sample s)**: z = (x̄ - μ₀) / (s/√n) for n > 30

- **Two-sample z-test for means**: z = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)

- **Test for proportion**: z = (p̂ - p₀) / √[p₀(1-p₀)/n]

## Key Points

1. Hypothesis testing provides a formal framework for making data-driven decisions about population parameters.

2. The null hypothesis represents the status quo or no-effect assumption, while the alternative represents the research claim.

3. Type I and Type II errors are inversely related; reducing one typically increases the other.

4. The choice of significance level (α) depends on the consequences of errors in the specific application.

5. A p-value less than α leads to rejection of H₀; a p-value greater than α means failure to reject H₀.

6. One-tailed tests are used when the direction of effect is specified; two-tailed tests when any difference is of interest.

7. Tests of significances are essential in computer science for algorithm comparison, A/B testing, and quality assurance.

8. Statistical significance does not necessarily imply practical significance, especially with large samples.

## Common Mistakes

1. **Confusing "fail to reject" with "accept"**: We never prove the null hypothesis true; we only fail to find sufficient evidence against it.

2. **Ignoring the distinction between one-tailed and two-tailed tests**: Using the wrong test leads to incorrect conclusions.

3. **Misinterpreting p-values**: A p-value is not the probability that H₀ is true; it is the probability of the data given H₀ is true.

4. **Choosing inappropriate significance levels**: Using α = 0.05 without considering the context and consequences of errors.

5. **Overlooking assumptions**: Applying z-tests without checking sample size requirements or normality conditions when necessary.