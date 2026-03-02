# Linear and Logistic Regression - Summary

## Key Definitions and Concepts

- **Simple Linear Regression**: A statistical method modeling the relationship between one independent variable X and one continuous dependent variable Y using the equation Y = β₀ + β₁X + ε
- **Multiple Linear Regression**: Extension using multiple predictors: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε
- **Logistic Regression**: Classification algorithm predicting binary outcomes using the sigmoid function: P = 1/(1+e^-z) where z = β₀ + β₁X
- **Odds Ratio**: The exponentiated logistic coefficient (e^β) representing the change in odds for a one-unit increase in the predictor
- **Sigmoid Function**: S-shaped curve mapping any real number to [0,1] probability range
- **Cost Function**: MSE for linear regression; Log Loss (Binary Cross-Entropy) for logistic regression

## Important Formulas and Theorems

- **Linear Regression OLS**: β₁ = Σ(xi-x̄)(yi-ȳ) / Σ(xi-x̄)², β₀ = ȳ - β₁x̄
- **Matrix Form**: β = (XᵀX)⁻¹XᵀY
- **Sigmoid**: P(Y=1|X) = 1 / (1 + e^-(β₀ + β₁X))
- **Log-Odds**: log(P/(1-P)) = β₀ + β₁X
- **Gradient Descent Update**: βⱼ := βⱼ - α × (1/m) × Σ(h(x⁽ⁱ⁾) - y⁽ⁱ⁾)xⱼ⁽ⁱ⁾
- **R²**: 1 - (SSR/SST), measures variance explained by the model

## Key Points

- Linear regression predicts continuous outcomes; logistic regression predicts probabilities for binary classification
- The OLS method minimizes sum of squared residuals to find optimal coefficients
- Logistic regression coefficients represent changes in log-odds, not direct probability changes
- Odds ratios > 1 indicate increased odds of the outcome; < 1 indicate decreased odds
- Learning rate (α) in gradient descent must be chosen carefully—too small slows convergence, too large causes oscillation
- R² can artificially inflate with additional predictors; Adjusted R² penalizes model complexity
- Key linear regression assumptions: linearity, independence, homoscedasticity, normality of errors
- For logistic regression, threshold of 0.5 is default for class prediction but can be adjusted based on precision-recall tradeoffs

## Common Mistakes to Avoid

1. **Confusing regression with classification**: Linear regression outputs continuous values; logistic regression outputs probabilities that are thresholded for classification
2. **Ignoring assumption violations**: Applying linear regression without checking assumptions leads to unreliable predictions
3. **Interpreting logistic coefficients directly**: Coefficients represent log-odds changes; must exponentiate to get odds ratios
4. **Ignoring multicollinearity**: Highly correlated predictors in MLR inflate standard errors and make interpretation unreliable
5. **Using linear regression for binary outcomes**: Predictions can fall outside [0,1] range; logistic regression properly bounds probabilities

## Revision Tips

1. Practice deriving OLS coefficients from small datasets by hand—you may need to show workings in exams
2. Memorize the sigmoid function formula and be able to calculate probabilities for given z-values
3. Understand gradient descent conceptually: it iteratively moves parameters in the direction that reduces cost
4. Review past DU question papers to identify the pattern—usually 5-6 marks for derivation, 8-10 marks for problems
5. Create a comparison table between linear and logistic regression to remember key differences
6. Focus on interpretation: what does an odds ratio of 1.5 actually mean in a business context?