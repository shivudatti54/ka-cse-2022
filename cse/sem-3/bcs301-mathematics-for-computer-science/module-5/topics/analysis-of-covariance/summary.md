# Analysis of Covariance (ANCOVA) - Summary

## Key Definitions and Concepts

- **ANCOVA**: A statistical technique combining ANOVA and regression to compare group means while controlling for the effects of one or more continuous covariates
- **Covariate**: A continuous variable that is related to the dependent variable and is included in the analysis to reduce error variance
- **Adjusted Means (Least Squares Means)**: Group means after adjusting for the covariate, representing what the means would be if all groups had the same average covariate value
- **Homogeneity of Regression Slopes**: The assumption that the relationship between the covariate and dependent variable is consistent across all treatment groups

## Important Formulas and Theorems

- **General Linear Model**: Y_ij = μ + τ_i + β(X_ij - X̄) + ε_ij
- **Adjusted Mean Formula**: Ȳ_i(adjusted) = Ȳ_i - b(X̄_i - X̄)
- **Partitioning of Variance**: Total SS = Treatment SS + Covariate SS + Error SS

## Key Points

1. ANCOVA increases precision by removing variability due to the covariate from the error term
2. Six assumptions must be satisfied: linearity, homogeneity of regression slopes, independence, normality, homoscedasticity, and covariate measurement accuracy
3. The homogeneity of regression slopes assumption is tested using an interaction term (covariate × group)
4. One-way ANCOVA involves one categorical factor and one covariate
5. Two-way ANCOVA involves two categorical factors and can include one or more covariates
6. ANCOVA can detect smaller treatment effects than equivalent ANOVA due to reduced error variance
7. The covariate should be reliably measured to avoid biased estimates

## Common Mistakes to Avoid

- Running ANCOVA without checking the assumptions, especially homogeneity of regression slopes
- Including a covariate that is affected by the treatment (not just affecting the outcome)
- Interpreting unadjusted group means instead of adjusted means when covariate groups differ
- Using ANCOVA when the relationship between covariate and dependent variable is non-linear

## Revision Tips

1. Practice writing out the ANCOVA model equation for different scenarios
2. Work through numerical examples to understand adjusted mean calculations
3. Memorize all six assumptions and know how to test each one
4. Review the difference between ANOVA and ANCOVA in terms of precision and power
5. Understand that ANCOVA is essentially ANOVA on residuals after regression adjustment
