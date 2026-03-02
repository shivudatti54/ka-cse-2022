# Chi Square Distribution - Summary

## Key Definitions

- **Chi Square Distribution (χ²)**: The probability distribution of the sum of squares of k independent standard normal random variables, denoted as χ²(k) where k is the degrees of freedom.

- **Degrees of Freedom**: The number of independent observations minus the number of estimated parameters, determining the shape of the Chi Square distribution.

- **Contingency Table**: A table showing the frequency distribution of variables to test independence between categorical variables.

- **Expected Frequency**: The frequency expected under the null hypothesis, calculated as (Row Total × Column Total) / Grand Total.

## Important Formulas

- **PDF**: f(x; k) = (1/[2^(k/2)Γ(k/2)]) × x^(k/2-1) × e^(-x/2), x > 0

- **Mean**: E[X] = k

- **Variance**: Var(X) = 2k

- **Test of Independence**: χ² = Σ(Oij - Eij)²/Eij with df = (r-1)(c-1)

- **Goodness of Fit**: χ² = Σ(Oi - Ei)²/Ei with df = k - 1 - m

## Key Points

1. The Chi Square distribution is derived from the sum of squares of k independent standard normal variables.

2. It is a special case of the Gamma distribution with parameters α = k/2 and β = 2.

3. The distribution is always right-skewed and approaches normality as degrees of freedom increase.

4. Chi Square tests are exclusively right-tailed tests for hypothesis testing.

5. Expected frequencies must be at least 5 for the Chi Square approximation to be valid.

6. The degrees of freedom depend on the specific test: (r-1)(c-1) for independence, (k-1-m) for goodness of fit.

7. Applications in CS include database attribute independence testing, feature selection in ML, and quality metrics analysis.

8. The test statistic is always non-negative, equaling zero only when observed equals expected exactly.

## Common Mistakes

1. **Using wrong degrees of freedom**: Students often forget to subtract 1 from both rows and columns when calculating df for independence tests.

2. **Ignoring minimum frequency requirement**: Applying Chi Square test when expected frequencies are less than 5 leads to unreliable results.

3. **Confusing one-tailed and two-tailed tests**: Chi Square tests are always one-tailed (right tail), not two-tailed.

4. **Forgetting to estimate parameters**: In goodness of fit, failing to subtract the number of estimated parameters (m) from (k-1) when calculating degrees of freedom.