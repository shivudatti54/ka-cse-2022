# Introduction to Linear Regression - Summary

## Key Definitions and Concepts

- **Linear Regression**: A supervised learning algorithm that models the relationship between a dependent variable (y) and one or more independent variables (x) using a linear function.

- **Simple Linear Regression**: Regression with ONE independent variable, expressed as y = wx + b where w is the weight/slope and b is the bias/intercept.

- **Multiple Linear Regression**: Regression with MULTIPLE independent variables, expressed as y = w₁x₁ + w₂x₂ + ... + wₙxₙ + b.

- **Cost Function**: A metric that measures the error of the model; for linear regression, typically Mean Squared Error (MSE) = (1/n)Σ(yᵢ - ŷᵢ)².

- **Ordinary Least Squares (OLS)**: The analytical method that finds optimal parameters by minimizing the sum of squared residuals.

- **Gradient Descent**: An iterative optimization algorithm that updates parameters by moving in the direction opposite to the gradient of the cost function.

## Important Formulas and Theorems

- **Simple Linear Regression Slope**: m = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²
- **Simple Linear Regression Intercept**: c = ȳ - mx̄
- **Multiple Regression (Matrix Form)**: w = (XᵀX)⁻¹Xᵀy
- **Gradient Descent Update (weights)**: w := w - α × (∂MSE/∂w)
- **R-squared**: R² = 1 - (SSR/SST) = 1 - Σ(yᵢ - ŷᵢ)² / Σ(yᵢ - ȳ)²

## Key Points

- Linear regression assumes a LINEAR relationship between variables; always visualize data first.

- The OLS method provides the BEST LINEAR UNBIASED ESTIMATOR under certain assumptions (Gauss-Markov theorem).

- The learning rate (α) in gradient descent must be chosen carefully: too small = slow convergence, too large = may not converge.

- R² CAN increase simply by adding predictors; use ADJUSTED R² to compare models with different numbers of features.

- Five assumptions must hold for valid inference: linearity, independence, homoscedasticity, normality, and no multicollinearity.

- RMSE is in the SAME UNITS as the target variable, making it more interpretable than MSE.

- Regularization techniques (Ridge, Lasso) address overfitting in high-dimensional data.

## Common Mistakes to Avoid

- CONFUSING correlation with causation: a strong linear relationship does not imply one variable causes the other.

- IGNORING assumptions: applying linear regression without checking assumptions produces unreliable results.

- OVERFITTING by including too many features without proper validation; the model may perform poorly on new data.

- USING the model outside the RANGE of training data (extrapolation) can lead to highly inaccurate predictions.

- NOT standardizing/normalizing features when using gradient descent or regularization; features with large scales dominate the learning.

## Revision Tips

- PRACTICE numerical problems: calculate means, slopes, intercepts, and predictions by hand for small datasets.

- MEMORIZE the five assumptions and be able to explain how to check each one graphically.

- UNDERSTAND the geometric interpretation: regression finds the line (or hyperplane) that minimizes the sum of squared perpendicular distances to data points.

- SOLVE previous year DU exam questions to familiarize yourself with the exam pattern and important topics.

- CREATE a flowchart for choosing between simple vs. multiple regression and for selecting evaluation metrics.