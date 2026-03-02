# F-Distribution - Summary

## Key Definitions and Concepts

- **F-Distribution**: A continuous probability distribution defined as the ratio of two independent chi-square variables divided by their respective degrees of freedom: F = (U/d₁)/(V/d₂) ~ F(d₁, d₂)
- **F-Statistic**: The test statistic used in F-tests, calculated as the ratio of two sample variances: F = s₁²/s₂² (with s₁² ≥ s₂²)
- **Degrees of Freedom**: Two parameters (d₁, d₂) where d₁ = numerator df = n₁ - 1 and d₂ = denominator df = n₂ - 1
- **Critical Value**: The F value from statistical tables corresponding to a specific significance level α and degrees of freedom (d₁, d₂)

## Important Formulas and Theorems

- **F-statistic for variance comparison**: F = s₁²/s₂² where s₁² and s₂² are sample variances
- **Mean of F-distribution**: E[F] = d₂/(d₂ - 2) for d₂ > 2
- **Relationship with t-distribution**: If t ~ t(d), then t² ~ F(1, d)
- **ANOVA F-statistic**: F = MSBetween/MSWithin where MS = Sum of Squares/df

## Key Points

- F-distribution is always positive and right-skewed; skewness decreases as degrees of freedom increase
- The F-test is exclusively a right-tailed test comparing ratios of variances
- Always place the larger sample variance in the numerator to ensure F ≥ 1
- As degrees of freedom increase, F-distribution approaches a normal distribution with mean ≈ 1
- ANOVA uses F-distribution to test whether all group means are equal
- In regression analysis, F-test determines if the overall model is statistically significant
- Key assumptions: independent random samples from normally distributed populations

## Common Mistakes to Avoid

- Confusing numerator and denominator degrees of freedom when reading F-tables
- Using F-test for comparing means instead of variances (use t-test for means)
- Forgetting to check normality assumption, which is critical for valid F-test results
- Placing the smaller variance in numerator, which leads to incorrect F < 1 values

## Revision Tips

- Memorize the relationship F(1, n) = t²(n) for quick conversions between tests
- Practice reading F-tables for common significance levels (0.05, 0.01) and typical df combinations
- Focus on understanding when to apply F-test versus other statistical tests
- Remember that F = 1 when population variances are equal; significant deviation from 1 indicates inequality