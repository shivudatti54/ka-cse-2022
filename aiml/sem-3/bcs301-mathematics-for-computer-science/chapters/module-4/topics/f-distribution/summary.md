# F-Distribution - Summary

## Key Definitions and Concepts

- **F-Distribution**: A continuous probability distribution defined as the ratio of two independent chi-squared random variables divided by their respective degrees of freedom: F = (U/d1)/(V/d2) ~ F(d1, d2)

- **F-Statistic**: The ratio of two sample variances, F = s1²/s2², used for comparing population variances

- **Numerator Degrees of Freedom (d1)**: Degrees of freedom associated with the chi-squared variable in the numerator

- **Denominator Degrees of Freedom (d2)**: Degrees of freedom associated with the chi-squared variable in the denominator

- **ANOVA**: Analysis of Variance, a statistical method that uses F-distribution to compare means across multiple groups

## Important Formulas and Theorems

- **F-Distribution Definition**: If U ~ χ²(d1) and V ~ χ²(d2) are independent, then F = (U/d1)/(V/d2) ~ F(d1, d2)

- **Mean of F-distribution**: E[F] = d2/(d2 - 2) for d2 > 2

- **F-statistic for variance comparison**: F = s1²/s2² with (n1-1, n2-1) degrees of freedom

- **ANOVA F-statistic**: F = MS_between / MS_within, where MS = SS/df

- **Relationship to t-distribution**: If X ~ t(d), then X² ~ F(1, d)

## Key Points

- The F-distribution is only defined for positive values (x > 0) and is always positively skewed

- The F-distribution approaches normal distribution as both degrees of freedom increase

- In ANOVA, the F-test determines if between-group variance is significantly larger than within-group variance

- In regression, the F-test evaluates whether the regression model provides significant explanatory power

- The larger variance should typically be placed in the numerator when performing variance comparison tests

- The F-distribution is non-symmetric, and critical values differ for numerator and denominator degrees of freedom

## Common Mistakes to Avoid

- Confusing numerator and denominator degrees of freedom when reading F-tables or interpreting results

- Using F-distribution for negative values (it is only defined for x > 0)

- Forgetting that F-test is inherently right-tailed in most applications; left-tail critical values require transformation

- Misinterpreting a non-significant result as proof that variances are equal (failure to reject H0 ≠ acceptance H0)

- Not checking assumptions: independence of samples, normality of underlying populations

## Revision Tips

- Practice computing F-statistics from raw data by calculating sample variances first

- Memorize the relationship between F and t distributions as it frequently appears in exams

- Work through at least one complete ANOVA example to understand the flow of calculations

- Review F-tables for common significance levels (0.05 and 0.01) and degree combinations

- Understand the interpretation: F > 1 indicates more between-group variance than expected by chance