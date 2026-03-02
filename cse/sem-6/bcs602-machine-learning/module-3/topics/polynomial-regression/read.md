# Polynomial Regression

## 1. Introduction and Theoretical Foundations

Polynomial regression constitutes a fundamental extension of linear regression, enabling the modeling of non-linear relationships between independent and dependent variables through polynomial basis functions. This technique proves indispensable when the underlying data exhibits curvilinear patterns that cannot be adequately captured by simple linear models.

The fundamental premise of polynomial regression rests upon the recognition that numerous real-world phenomena exhibit non-linear characteristics. While linear regression assumes a straight-line relationship of the form Y = β₀ + β₁X, many physical, economic, and biological processes follow more complex patterns that require curved functional approximations.

## 2. Mathematical Formulation

### 2.1 General Polynomial Model

The general form of an n-th degree polynomial regression model is expressed as:

$$Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \beta_3 X^3 + \ldots + \beta_n X^n + \epsilon$$

Wherein:

- n denotes the polynomial degree (order)
- β₀, β₁, ..., βₙ represent the regression coefficients (parameters)
- ε signifies the random error term, typically assumed to follow N(0, σ²)

### 2.2 Common Polynomial Degrees

| Degree        | Model Form                        | Geometric Interpretation |
| ------------- | --------------------------------- | ------------------------ |
| 1 (Linear)    | Y = β₀ + β₁X                      | Straight line            |
| 2 (Quadratic) | Y = β₀ + β₁X + β₂X²               | Parabola                 |
| 3 (Cubic)     | Y = β₀ + β₁X + β₂X² + β₃X³        | S-curve                  |
| 4 (Quartic)   | Y = β₀ + β₁X + β₂X² + β₃X³ + β₄X⁴ | W-shaped curve           |

## 3. Linearity in Parameters: A Critical Distinction

Despite modeling non-linear relationships in the feature space, polynomial regression remains **linear in its parameters**. This fundamental property permits the application of ordinary least squares (OLS) estimation.

The model can be conceptualized as a linear combination:
$$Y = \sum_{j=0}^{n} \beta_j \phi_j(X)$$

Where φ_j(X) = X^j represents the j-th basis function. The "non-linearity" emerges from the transformed features (X², X³, etc.), not from the parameters themselves.

## 4. Ordinary Least Squares Estimation: Derivation

### 4.1 Feature Matrix Construction

Given a dataset {(x₁, y₁), (x₂, y₂), ..., (x_m, y_m)}, we construct the design matrix X ∈ ℝ^(m×(n+1)):

$$X = \begin{bmatrix} 1 & x_1 & x_1^2 & \ldots & x_1^n \\ 1 & x_2 & x_2^2 & \ldots & x_2^n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_m & x_m^2 & \ldots & x_m^n \end{bmatrix}$$

The coefficient vector β = [β₀, β₁, ..., βₙ]ᵀ and response vector y = [y₁, y₂, ..., y_m]ᵀ.

### 4.2 OLS Solution Derivation

The OLS estimator minimizes the residual sum of squares (RSS):

$$RSS(\beta) = \sum_{i=1}^{m} (y_i - \hat{y}_i)^2 = \|y - X\beta\|^2$$

Taking the derivative with respect to β and setting to zero:

$$\frac{\partial RSS}{\partial \beta} = -2X^T(y - X\beta) = 0$$

This yields the **normal equations**:

$$X^T X \beta = X^T y$$

Assuming X^T X is invertible (full column rank), the closed-form solution is:

$$\hat{\beta}_{OLS} = (X^T X)^{-1} X^T y$$

### 4.3 Statistical Properties

Under the classical assumptions (homoscedasticity, no autocorrelation, normally distributed errors), the OLS estimator possesses the following properties:

1. **Unbiasedness**: E(β̂) = β
2. **Minimum Variance**: Among all linear unbiased estimators, OLS achieves the minimum variance (Gauss-Markov theorem)
3. **Consistency**: As m → ∞, β̂ → β in probability

### 4.4 Practical Considerations: Singular Matrix

For high-degree polynomials, X^T X may become singular or near-singular (ill-conditioned). This occurs due to:

- Collinearity among polynomial features (X, X², X³ are highly correlated)
- Numerical instability in matrix inversion

**Solution**: Regularization (Ridge or Lasso) or pseudo-inverse computation.

## 5. Bias-Variance Tradeoff Analysis

The prediction error for polynomial regression comprises three components:

$$E[(y - \hat{f}(x))^2] = \text{Bias}^2(\hat{f}) + \text{Var}(\hat{f}) + \sigma^2$$

| Polynomial Degree | Bias²  | Variance  | Generalization | Risk |
| ----------------- | ------ | --------- | -------------- | ---- |
| Low (1-2)         | High   | Low       | Underfitting   | High |
| Medium (3-5)      | Medium | Medium    | Optimal        | Low  |
| High (>5)         | Low    | Very High | Overfitting    | High |

The bias decreases as degree increases (model becomes more flexible), while variance increases exponentially. The optimal degree minimizes total error.

## 6. Feature Scaling: Numerical Imperative

Higher-degree polynomial terms exhibit vastly different scales, causing severe numerical problems during optimization.

**Example**: For X ∈ [1, 100]

- X: range [1, 100]
- X²: range [1, 10,000]
- X³: range [1, 1,000,000]
- X⁴: range [1, 100,000,000]

**Without scaling**: The condition number of X^T X becomes extremely large, leading to:

- Numerical instability in matrix inversion
- Gradient descent convergence issues
- Coefficient magnitudes becoming uninterpretable

**Solution**: Apply standardization (z-score normalization) before polynomial feature creation:

$$x_{scaled} = \frac{x - \mu_x}{\sigma_x}$$

## 7. Regularization: Preventing Overfitting

### 7.1 Ridge Regression (L2 Regularization)

Adds penalty term λ∑βⱼ² to the objective:

$$\hat{\beta}_{Ridge} = \arg\min_\beta \left\{ \|y - X\beta\|^2 + \lambda \sum_{j=1}^{n} \beta_j^2 \right\}$$

**Solution**: $\hat{\beta}_{Ridge} = (X^T X + \lambda I)^{-1} X^T y$

Ridge regression shrinks all coefficients proportionally, with higher-degree terms experiencing greater shrinkage.

### 7.2 Lasso Regression (L1 Regularization)

Adds penalty term λ∑|βⱼ|:

$$\hat{\beta}_{Lasso} = \arg\min_\beta \left\{ \|y - X\beta\|^2 + \lambda \sum_{j=1}^{n} |\beta_j| \right\}$$

Lasso performs feature selection by driving some coefficients exactly to zero, effectively selecting the optimal polynomial terms.

### 7.3 Elastic Net

Combines L1 and L2 penalties: λ(ρ∑|βⱼ| + (1-ρ)∑βⱼ²/2)

## 8. Degree Selection Methods

### 8.1 Cross-Validation

K-fold cross-validation provides an unbiased estimate of generalization error:

1. Split data into K folds
2. Train polynomial models of degrees d = 1, 2, ..., D
3. For each degree, compute average validation error across K folds
4. Select degree with minimum validation error

### 8.2 Adjusted R²

$$R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

Where p is the number of predictors. This penalizes unnecessary complexity.

### 8.3 Akaike Information Criterion (AIC)

$$AIC = m \ln\left(\frac{RSS}{m}\right) + 2k$$

Where k = p + 1 (number of parameters). Lower AIC indicates better model.

## 9. Multivariate Polynomial Regression

When multiple independent variables exist, polynomial regression extends to interaction terms:

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_1^2 + \beta_4 X_2^2 + \beta_5 X_1 X_2 + \ldots + \epsilon$$

The feature space grows exponentially: for d variables with degree n, the number of terms is:

$$\binom{d + n}{n}$$

## 10. Comparative Analysis

| Aspect                 | Polynomial Regression | Kernel Methods (SVM) | Neural Networks         |
| ---------------------- | --------------------- | -------------------- | ----------------------- |
| Interpretability       | Moderate              | Low                  | Low                     |
| Feature Engineering    | Manual                | Implicit (kernel)    | Automatic               |
| Scalability            | Poor (high degree)    | Moderate             | Excellent               |
| Theoretical Foundation | Established           | Strong               | Empirical               |
| Overfitting Control    | Regularization        | Margin maximization  | Dropout, early stopping |

## 11. Practical Implementation Considerations

### 11.1 Python Implementation with scikit-learn

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

# Create polynomial regression pipeline
poly_model = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=3)),
    ('regressor', Ridge(alpha=1.0))
])

# Fit and evaluate
poly_model.fit(X_train, y_train)
scores = cross_val_score(poly_model, X_val, y_val, cv=5)
```

### 11.2 Avoiding Runge's Phenomenon

High-degree polynomials exhibit oscillations at domain boundaries (Runge's phenomenon). Mitigation strategies include:

- Using lower-degree polynomials
- Applying regularization
- Employing splines (piecewise polynomials)
- Ensuring sufficient data points across the domain

---

## Exam Tips and Key Takeaways

1. **Fundamental Concept**: Polynomial regression is linear in parameters (β), non-linear in features (X, X², X³, ...)
2. **OLS Derivation**: Remember the closed-form solution β̂ = (XᵀX)⁻¹Xᵀy and understand conditions for its validity
3. **Bias-Variance**: Higher degree → lower bias, higher variance; optimal degree balances both
4. **Feature Scaling**: Always normalize before creating polynomial terms to prevent numerical instability
5. **Regularization**: Ridge shrinks coefficients; Lasso can eliminate terms; both prevent overfitting
6. **Degree Selection**: Cross-validation provides reliable estimates; avoid AIC/R² alone for degree selection
