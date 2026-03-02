# Covariance and Correlation Coefficients - Summary

## Key Definitions and Concepts

- **Covariance:** A measure of joint variability between two random variables, indicating whether they tend to move together. Formula: Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E(XY) - E(X)E(Y)

- **Correlation Coefficient (Pearson's r):** A standardized measure of linear relationship between two variables, ranging from -1 to +1. Formula: r = Cov(X, Y) / (σₓ · σᵧ)

- **Sample Covariance:** sₓᵧ = (1/(n-1)) Σᵢ(xᵢ - x̄)(yᵢ - ȳ)

- **Sample Correlation:** r = sₓᵧ / (sₓ · sᵧ)

## Important Formulas and Theorems

- Covariance in terms of correlation: Cov(X, Y) = r · σₓ · σᵧ
- Covariance from expectations: Cov(X, Y) = E(XY) - E(X)E(Y)
- Variance of sum: Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)
- Property: Cov(aX + b, cY + d) = ac · Cov(X, Y)

## Key Points

1. Positive covariance/correlation indicates variables move in the same direction; negative indicates opposite directions
2. Correlation coefficient is dimensionless and always bounded between -1 and +1
3. Zero covariance implies independence only for normally distributed variables
4. |r| ≥ 0.7: Strong, |r| 0.4-0.7: Moderate, |r| < 0.2: Weak correlation
5. Covariance is symmetric: Cov(X, Y) = Cov(Y, X)
6. Cov(X, X) = Var(X), making variance a special case of covariance
7. Correlation is invariant to scaling and translation of variables
8. Perfect linear relationships have correlation of exactly +1 or -1

## Common Mistakes to Avoid

1. **Assuming zero covariance means independence:** This is only true for jointly normal distributions
2. **Ignoring scale:** Covariance values depend on variable scales and cannot be compared across different datasets
3. **Confusing correlation with causation:** High correlation does not mean one variable causes changes in another
4. **Forgetting the n-1 denominator:** Sample covariance uses (n-1), not n, for unbiased estimation

## Revision Tips

1. Practice calculating both covariance and correlation from raw data tables multiple times
2. Create a property checklist and verify each property with simple examples
3. Work through problems involving joint probability distributions (both discrete and continuous)
4. Relate concepts to ML applications—understand why correlation matters in feature selection
5. Memorize the interpretation guidelines for correlation values (strong, moderate, weak)
6. Review the relationship formula: r = Cov/(σₓσᵧ)—this connects all major concepts