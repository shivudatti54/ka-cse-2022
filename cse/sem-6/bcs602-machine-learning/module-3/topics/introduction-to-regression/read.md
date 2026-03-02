# Introduction to Regression Analysis

## 1. Fundamental Concepts and Definition

Regression analysis constitutes a cornerstone of statistical methodology and machine learning, representing a supervised learning paradigm wherein the objective is to predict continuous numerical outcomes by establishing a functional relationship between predictor (independent) variables and a target (dependent) variable. Unlike classification tasks that assign observations to discrete categorical labels, regression quantifies the magnitude of relationships and forecasts specific numerical values, rendering it indispensable for predictive analytics across diverse domains.

Formally, let $Y$ denote the dependent variable and $X = (X_1, X_2, ..., X_p)$ represent a vector of $p$ independent variables. The fundamental regression model posits:

$$Y = f(X) + \epsilon$$

where $f: \mathbb{R}^p \rightarrow \mathbb{R}$ denotes the unknown regression function characterizing the systematic relationship, and $\epsilon$ represents the random error term, typically assumed to have zero mean and finite variance. The primary objective of regression analysis is to estimate $\hat{f}(X)$, an approximation of the true function $f(X)$, from observed data $\{(x_i, y_i)\}_{i=1}^{n}$.

## 2. Distinction Between Regression and Classification

Understanding the fundamental dichotomy between regression and classification is essential for appropriate methodology selection:

| Criterion                     | Regression                                                         | Classification                                          |
| ----------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------- |
| **Output Space**              | Continuous $\mathbb{R}$                                            | Discrete $\{c_1, c_2, ..., c_k\}$                       |
| **Objective**                 | Predict numerical magnitude                                        | Assign categorical labels                               |
| **Evaluation Metrics**        | MSE, RMSE, MAE, $R^2$                                              | Accuracy, Precision, Recall, F1-score, AUC              |
| **Loss Functions**            | Squared error, Absolute error                                      | Cross-entropy, Hinge loss                               |
| **Illustrative Applications** | House price estimation, temperature forecasting, demand prediction | Spam detection, image categorization, medical diagnosis |

## 3. Mathematical Framework for Linear Regression

### 3.1 Model Specification

Consider a dataset comprising $n$ observations and $p$ predictor variables. In matrix notation, the linear regression model is expressed as:

$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$$

where $\mathbf{y} \in \mathbb{R}^n$ denotes the vector of observed responses, $\mathbf{X} \in \mathbb{R}^{n \times (p+1)}$ represents the design matrix (including a column of ones for the intercept term), $\boldsymbol{\beta} \in \mathbb{R}^{p+1}$ signifies the vector of regression coefficients, and $\boldsymbol{\epsilon} \in \mathbb{R}^n$ represents the error vector.

### 3.2 Ordinary Least Squares (OLS) Estimation

The Ordinary Least Squares (OLS) methodology seeks coefficients that minimize the Residual Sum of Squares (RSS):

$$\text{RSS}(\boldsymbol{\beta}) = \sum_{i=1}^{n}(y_i - \mathbf{x}_i^T\boldsymbol{\beta})^2 = \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2$$

**Derivation of Normal Equations:**

Taking the gradient of RSS with respect to $\boldsymbol{\beta}$ and setting it to zero:

$$\frac{\partial \text{RSS}}{\partial \boldsymbol{\beta}} = -2\mathbf{X}^T(\mathbf{y} - \mathbf{X}\boldsymbol{\beta}) = \mathbf{0}$$

This yields the **normal equations**:

$$\mathbf{X}^T\mathbf{X}\boldsymbol{\beta} = \mathbf{X}^T\mathbf{y}$$

Under the assumption that $\mathbf{X}^T\mathbf{X}$ is invertible (i.e., columns of $\mathbf{X}$ are linearly independent), the OLS estimator is:

$$\boxed{\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}}$$

### 3.3 Properties of OLS Estimators (Gauss-Markov Theorem)

Under the Gauss-Markov assumptions:

1. $\mathbb{E}[\boldsymbol{\epsilon}] = \mathbf{0}$ (zero mean errors)
2. $\text{Var}(\boldsymbol{\epsilon}) = \sigma^2 \mathbf{I}$ (homoscedasticity, uncorrelated errors)
3. $\mathbf{X}$ is non-stochastic with full column rank

The OLS estimator $\hat{\boldsymbol{\beta}}$ possesses the following properties:

- **Unbiasedness**: $\mathbb{E}[\hat{\boldsymbol{\beta}}] = \boldsymbol{\beta}$
- **Minimum Variance**: Among all linear unbiased estimators, OLS achieves the smallest variance (Best Linear Unbiased Estimator - BLUE)

The variance-covariance matrix is:

$$\text{Var}(\hat{\boldsymbol{\beta}}) = \sigma^2 (\mathbf{X}^T\mathbf{X})^{-1}$$

The error variance $\sigma^2$ is estimated by:

$$\hat{\sigma}^2 = \frac{\text{RSS}}{n - p - 1}$$

### 3.4 Gradient Descent Optimization

For large-scale problems where computing $(\mathbf{X}^T\mathbf{X})^{-1}$ is computationally prohibitive, gradient descent provides an iterative alternative:

**Objective Function**: $J(\boldsymbol{\beta}) = \frac{1}{2n}\sum_{i=1}^{n}(h_\boldsymbol{\beta}(x_i) - y_i)^2$

**Update Rule**: $\boldsymbol{\beta} := \boldsymbol{\beta} - \alpha \nabla J(\boldsymbol{\beta})$

where $\alpha > 0$ denotes the learning rate. For linear regression, the gradient simplifies to:

$$\frac{\partial J}{\partial \beta_j} = \frac{1}{n}\sum_{i=1}^{n}(h_\boldsymbol{\beta}(x_i) - y_i)x_{ij}$$

**Algorithm Pseudocode**:

```
Initialize β to random values
repeat until convergence:
    for j = 0 to p:
        β_j := β_j - α × (1/n) × Σ(h(x_i) - y_i) × x_ij
```

## 4. Regularization Methods

### 4.1 Ridge Regression (L2 Regularization)

Ridge regression modifies the OLS objective by adding an L2 penalty term:

$$\hat{\boldsymbol{\beta}}^{\text{ridge}} = \arg\min_{\boldsymbol{\beta}} \left\{ \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2 + \lambda \|\boldsymbol{\beta}\|_2^2 \right\}$$

The closed-form solution is:

$$\hat{\boldsymbol{\beta}}^{\text{ridge}} = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$$

Ridge regression **shrinks** coefficients toward zero but **never** sets them exactly to zero, thereby retaining all predictors while reducing variance.

### 4.2 Lasso Regression (L1 Regularization)

Lasso employs an L1 penalty:

$$\hat{\boldsymbol{\beta}}^{\text{lasso}} = \arg\min_{\boldsymbol{\beta}} \left\{ \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2 + \lambda \|\boldsymbol{\beta}\|_1 \right\}$$

Unlike ridge, Lasso performs **feature selection** by driving some coefficients to exactly zero, producing sparse models.

### 4.3 Elastic Net

Elastic Net combines both penalties:

$$\hat{\boldsymbol{\beta}}^{\text{elastic}} = \arg\min_{\boldsymbol{\beta}} \left\{ \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2 + \lambda_1 \|\boldsymbol{\beta}\|_1 + \lambda_2 \|\boldsymbol{\beta}\|_2^2 \right\}$$

This approach mitigates limitations of both ridge (when $p > n$) and lasso (when predictors are highly correlated).

## 5. Model Evaluation Metrics

### 5.1 Coefficient of Determination ($R^2$)

$$R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} = 1 - \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2}$$

Interpretation: Proportion of variance in the dependent variable explained by the model. Range: $[0, 1]$, where $R^2 = 1$ indicates perfect prediction.

### 5.2 Adjusted $R^2$

$$R_{\text{adj}}^2 = 1 - \frac{(1 - R^2)(n - 1)}{n - p - 1}$$

This metric penalizes unnecessary predictor inclusion and enables comparison across models with varying dimensionality.

### 5.3 Mean Squared Error (MSE)

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

Quadratic penalty emphasizes large errors.

### 5.4 Root Mean Squared Error (RMSE)

$$\text{RMSE} = \sqrt{\text{MSE}}$$

Interprets error in original units of the target variable.

### 5.5 Mean Absolute Error (MAE)

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

Robust to outliers; linear penalty for all errors.

## 6. Bias-Variance Tradeoff

For a given input $x_0$, the expected prediction error decomposes as:

$$\mathbb{E}[(y_0 - \hat{f}(x_0))^2] = \text{Var}(\hat{f}(x_0)) + [\text{Bias}(\hat{f}(x_0))]^2 + \text{Var}(\epsilon)$$

- **Bias**: Error from overly simplistic assumptions (e.g., fitting a linear model to quadratic data)
- **Variance**: Error from model sensitivity to training data fluctuations

The regularization parameter $\lambda$ in ridge/lasso controls this tradeoff: larger $\lambda$ increases bias but decreases variance.

## 7. Assumptions of Linear Regression

The validity of OLS inference rests upon fundamental assumptions:

1. **Linearity**: $Y = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$ correctly specifies the relationship
2. **Exogeneity**: $\mathbb{E}[\boldsymbol{\epsilon}|\mathbf{X}] = \mathbf{0}$ (no omitted variable bias)
3. **Homoscedasticity**: $\text{Var}(\epsilon_i) = \sigma^2$ constant across all $x_i$
4. **No autocorrelation**: $\text{Cov}(\epsilon_i, \epsilon_j) = 0$ for $i \neq j$
5. **Normality**: $\boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \sigma^2\mathbf{I})$ (for inference)
6. **No perfect multicollinearity**: $\text{rank}(\mathbf{X}) = p + 1$

Violations necessitate remedial measures (transformations, robust standard errors, generalized least squares).

## 8. Numerical Example: Simple Linear Regression

Given data points $(x, y)$: $(1, 2), (2, 3), (3, 5), (4, 4), (5, 5)$

For model $y = \beta_0 + \beta_1 x$:

Calculating using OLS formulas:

- $\bar{x} = 3$, $\bar{y} = 3.8$
- $\beta_1 = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2} = \frac{7}{10} = 0.7$
- $\beta_0 = \bar{y} - \beta_1\bar{x} = 3.8 - 0.7(3) = 1.7$

Thus: $\hat{y} = 1.7 + 0.7x$

Residual for $x=4$: $y_{actual} = 4$, $y_{pred} = 1.7 + 0.7(4) = 4.5$, residual = $-0.5$

## 9. Implementation Example

```python
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# OLS Regression
model_ols = LinearRegression()
model_ols.fit(X_train, y_train)
y_pred = model_ols.predict(X_test)

# Ridge Regression (L2 regularization)
model_ridge = Ridge(alpha=1.0)
model_ridge.fit(X_train, y_train)

# Lasso Regression (L1 regularization)
model_lasso = Lasso(alpha=1.0)
model_lasso.fit(X_train, y_train)

# Evaluation
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

---

## Assessment Questions

**Question 1 (Application)**: For a simple linear regression model fitted to data with $\sum(x_i - \bar{x})^2 = 100$, $\sum(x_i - \bar{x})(y_i - \bar{y}) = 50$, and $\bar{y} = 10$, what is the predicted value when $x = 5$?

(A) 12.5  
(B) 10.5  
(C) 15.0  
(D) 7.5

**Question 2 (Analysis)**: Given a ridge regression model with $\lambda = 0$, compare the coefficient estimates to ordinary least squares. What happens as $\lambda$ increases significantly?

(A) Coefficients remain unchanged regardless of $\lambda$  
(B) Coefficients shrink toward zero but never reach exactly zero  
(C) Some coefficients become exactly zero  
(D) Coefficients increase in magnitude

**Question 3 (Computation)**: Which of the following evaluation metrics is most appropriate when large prediction errors are particularly undesirable?

(A) MAE  
(B) RMSE  
(C) $R^2$  
(D) All are equally appropriate

**Question 4 (Conceptual)**: In the bias-variance decomposition, as model complexity increases:

(A) Bias decreases, variance increases  
(B) Bias increases, variance decreases  
(C) Both bias and variance decrease  
(D) Neither changes significantly
