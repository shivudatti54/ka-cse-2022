# F Distribution - Summary

## Key Definitions

- **F Distribution:** A continuous probability distribution defined as the ratio of two independent chi-squared variables divided by their respective degrees of freedom: F = (U/df₁) / (V/df₂), where U ~ χ²(df₁) and V ~ χ²(df₂)
- **Degrees of Freedom (df₁, df₂):** Two parameters representing the numerator and denominator degrees of freedom that completely characterize the F distribution
- **F-Test:** A statistical test using the F distribution to compare two population variances or to test nested models in regression
- **Critical Value (Fα):** The value such that P(F > Fα) = α for a given significance level

## Important Formulas

- **PDF:** f(x) = (df₁^(df₁/2) × df₂^(df₂/2) × x^(df₁/2 - 1)) / (B(df₁/2, df₂/2) × (df₁x + df₂)^((df₁+df₂)/2)), x > 0

- **Mean:** E[F] = df₂/(df₂ - 2), for df₂ > 2

- **Variance:** Var(F) = (2df₂²(df₁ + df₂ - 2)) / (df₁(df₂ - 2)²(df₂ - 4)), for df₂ > 4

- **F-Test Statistic:** F = s₁²/s₂², where s₁² and s₂² are sample variances from two independent samples

- **Relationship to t-distribution:** If T ~ t(ν), then T² ~ F(1, ν)

## Key Points

1. The F distribution is inherently non-negative and right-skewed, becoming more symmetric as degrees of freedom increase

2. Two independent parameters (df₁, df₂) fully characterize the distribution, unlike distributions with single parameters

3. The F distribution is fundamental to ANOVA, where it tests whether between-group variance exceeds within-group variance

4. In regression analysis, the F-test determines whether the addition of predictor variables significantly improves the model

5. The distribution connects to chi-squared through its definition and to Student's t through the squaring relationship

6. For comparing variances, always place the hypothesized larger variance in the numerator to simplify interpretation

7. As df₁, df₂ → ∞, the F distribution approaches a normal distribution (Central Limit Theorem)

8. Computer science applications include algorithm comparison, performance benchmarking, and experimental design

## Common Mistakes

1. **Confusing numerator and denominator degrees of freedom:** Always identify which sample corresponds to df₁ and which to df₂ in the F-ratio

2. **Using wrong tail for hypothesis test:** Some tests require left-tail critical values; ensure your alternative hypothesis matches the test direction

3. **Ignoring conditions on degrees of freedom:** The mean exists only for df₂ > 2 and variance only for df₂ > 4; don't apply formulas blindly

4. **Incorrect orientation of variance ratio:** When testing H₀: σ₁² = σ₂², always verify whether you're testing for greater-than or not-equal alternatives

5. **Forgetting that F is always positive:** Rejecting solutions with negative F-values indicates fundamental misunderstanding of the distribution