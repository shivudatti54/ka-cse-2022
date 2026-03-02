# Linear Regression

## 1. Introduction

Linear regression is a fundamental supervised learning algorithm that models the relationship between a continuous dependent variable (target) and one or more independent variables (features) by fitting a linear equation to the observed data. The core assumption is that the relationship between variables can be approximated by a straight line (in simple regression) or a hyperplane (in multiple regression).

This method dates back to the early 19th century with Legendre's and Gauss's work on least squares. Today, it remains one of the most widely used statistical and machine learning techniques due to its interpretability, computational efficiency, and strong theoretical foundation.

## 2. Mathematical Formulation

### 2.1 Simple Linear Regression

Simple linear regression models the relationship between one feature variable x and a continuous target variable y using a straight line:

$$y = wx + b$$

Where:

- **y**: Predicted value (target variable)
- **x**: Input feature (independent variable)
- **w**: Weight (slope) - represents the change in y per unit change in x
- **b**: Bias (intercept) - the value of y when x = 0

The objective is to find values of w and b that minimize the discrepancy between predicted and actual values.

### 2.2 Multiple Linear Regression

When multiple features are present, the model extends to:

$$y = w_1x_1 + w_2x_2 + ... + w_nx_n + b$$

In vectorized form, for a dataset with n samples and d features:

$$\mathbf{y} = \mathbf{X}\mathbf{w} + b$$

Where:

- $\mathbf{y} \in \mathbb{R}^{n \times 1}$ is the target vector
- $\mathbf{X} \in \mathbb{R}^{n \times d}$ is the feature matrix
- $\mathbf{w} \in \mathbb{R}^{d \times 1}$ is the weight vector
- $b \in \mathbb{R}$ is the bias term

By absorbing the bias into the weight vector using an augmented feature matrix (adding a column of ones to X), we can write:

$$\mathbf{y} = \mathbf{X}\mathbf{w}$$

## 3. The Ordinary Least Squares (OLS) Method

### 3.1 Cost Function: Mean Squared Error

The OLS method minimizes the sum of squared residuals (differences between actual and predicted values):

$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 = \frac{1}{n}||\mathbf{y} - \mathbf{X}\mathbf{w}||^2$$

This quadratic cost function is convex and has a unique global minimum, making it suitable for optimization.

### 3.2 Normal Equation (Closed-form Solution)

The normal equation provides a direct analytical solution for the optimal weights. To derive it, we set the gradient of the MSE with respect to weights to zero:

**Derivation:**
$$MSE = \frac{1}{n}(\mathbf{y} - \mathbf{X}\mathbf{w})^T(\mathbf{y} - \mathbf{X}\mathbf{w})$$

Taking the gradient:
$$\nabla_{\mathbf{w}} MSE = \frac{2}{n}\mathbf{X}^T(\mathbf{X}\mathbf{w} - \mathbf{y})$$

Setting gradient to zero:
$$\mathbf{X}^T\mathbf{X}\mathbf{w} = \mathbf{X}^T\mathbf{y}$$

Assuming $\mathbf{X}^T\mathbf{X}$ is invertible (full column rank), the solution is:

$$\mathbf{w} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

This is the **normal equation**, providing the closed-form OLS solution.

**Computational Complexity:**

- Time: $O(nd^2 + d^3)$ where n = samples, d = features
- Space: $O(d^2)$

When $d > n$ or $\mathbf{X}^T\mathbf{X}$ is ill-conditioned, numerical instability occurs, requiring regularization or alternative methods.

### 3.3 Gradient Descent (Iterative Solution)

For large datasets or high-dimensional problems, gradient descent provides an iterative approach:

**Derivation of Update Rules:**

Given MSE = $\frac{1}{n}\sum_{i=1}^{n}(y_i - \mathbf{w}^T\mathbf{x}_i)^2$

The partial derivative with respect to each weight $w_j$:
$$\frac{\partial}{\partial w_j}MSE = -\frac{2}{n}\sum_{i=1}^{n}x_{ij}(y_i - \mathbf{w}^T\mathbf{x}_i)$$

The gradient descent update rule:
$$w_j = w_j - \alpha \cdot \frac{\partial}{\partial w_j}MSE$$

Where $\alpha > 0$ is the learning rate controlling step size.

**Algorithm:**

```
Initialize w randomly
Repeat until convergence:
    compute predictions: ŷ = Xw
    compute gradient: g = (2/n) * X^T(ŷ - y)
    update weights: w = w - α * g
```

**Computational Complexity:**

- Time: $O(n \cdot d \cdot k)$ where k = number of iterations
- Space: $O(d)$

**Learning Rate Selection:**

- Too small: slow convergence
- Too large: oscillations or divergence
- Adaptive methods (Adam, RMSprop) can help

## 4. Statistical Inference

### 4.1 Assumptions of Linear Regression

For valid statistical inference, the following assumptions must hold:

1. **Linearity**: $y = \mathbf{X}\mathbf{w} + \epsilon$, where $\epsilon$ is the error term
2. **Independence**: Errors are independent (no autocorrelation)
3. **Homoscedasticity**: $Var(\epsilon_i) = \sigma^2$ for all i (constant variance)
4. **Normality**: $\epsilon \sim N(0, \sigma^2)$ (errors are normally distributed)
5. **No Multicollinearity**: Features are not perfectly correlated (X has full column rank)

### 4.2 Coefficient Confidence Intervals

Under assumptions 1-5, the OLS estimator follows:

$$\mathbf{w} \sim N\left(\mathbf{w}_{true}, \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}\right)$$

The $(1-\alpha)\%$ confidence interval for $w_j$ is:

$$w_j \pm t_{\alpha/2, n-d} \cdot \hat{\sigma} \cdot \sqrt{[(\mathbf{X}^T\mathbf{X})^{-1}]_{jj}}$$

Where $\hat{\sigma}^2 = \frac{1}{n-d}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$ is the estimated error variance.

### 4.3 Hypothesis Testing

To test if a coefficient is significantly different from zero:

**Null Hypothesis**: $H_0: w_j = 0$ (feature has no effect)
**Alternative Hypothesis**: $H_1: w_j \neq 0$ (feature has significant effect)

The t-statistic:
$$t_j = \frac{w_j}{SE(w_j)}$$

Where $SE(w_j) = \hat{\sigma} \cdot \sqrt{[(\mathbf{X}^T\mathbf{X})^{-1}]_{jj}}$

Compare $|t_j|$ with critical value $t_{\alpha/2, n-d}$. If $|t_j| > t_{\alpha/2, n-d}$, reject $H_0$.

### 4.4 The Gauss-Markov Theorem

Under assumptions 1-5, the OLS estimator is the **Best Linear Unbiased Estimator (BLUE)**:

- **Best**: Minimum variance among all unbiased estimators
- **Linear**: Linear function of observed y
- **Unbiased**: $E[\mathbf{w}] = \mathbf{w}_{true}$

This guarantees optimality in the class of linear unbiased estimators.

## 5. Residual Diagnostics

### 5.1 Residual Analysis

Residuals $e_i = y_i - \hat{y}_i$ help verify assumptions:

**Checking Homoscedasticity:**

- Plot residuals vs. fitted values
- funnel shape indicates heteroscedasticity
- Breusch-Pagan test provides formal assessment

**Checking Normality:**

- Q-Q plot of residuals
- Shapiro-Wilk or Jarque-Bera test

**Checking Linearity:**

- Plot residuals vs. each predictor
- patterns indicate non-linearity

### 5.2 Influential Observations

Cook's Distance identifies influential points:
$$D_i = \frac{e_i^2}{d \cdot MSE}\left[\frac{h_{ii}}{(1-h_{ii})^2}\right]$$

Where $h_{ii}$ is the leverage (diagonal of hat matrix). Points with $D_i > 4/n$ warrant investigation.

## 6. Regularization

### 6.1 Ridge Regression (L2 Regularization)

Adds penalty for large coefficients:
$$Cost_{Ridge} = MSE + \lambda \sum_{j=1}^{d}w_j^2 = ||\mathbf{y} - \mathbf{X}\mathbf{w}||^2 + \lambda\mathbf{w}^T\mathbf{w}$$

Solution: $\mathbf{w}_{ridge} = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$

**Properties:**

- Shrinks coefficients toward zero but never exactly zero
- Reduces variance at cost of some bias
- Effective when features are highly correlated

### 6.2 Lasso Regression (L1 Regularization)

Adds penalty based on absolute values:
$$Cost_{Lasso} = MSE + \lambda \sum_{j=1}^{d}|w_j|$$

**Properties:**

- Can set coefficients exactly to zero (feature selection)
- Produces sparse models
- Solution requires iterative optimization (coordinate descent, LARS)

### 6.3 Elastic Net

Combines L1 and L2 penalties:
$$Cost = MSE + \lambda_1 \sum_{j=1}^{d}|w_j| + \lambda_2 \sum_{j=1}^{d}w_j^2$$

Useful when features are correlated and feature selection is desired.

## 7. Evaluation Metrics

| Metric      | Formula                              | Interpretation                         |
| ----------- | ------------------------------------ | -------------------------------------- | --- | ------------------ |
| MSE         | $\frac{1}{n}\sum(y_i - \hat{y}_i)^2$ | Lower is better                        |
| RMSE        | $\sqrt{MSE}$                         | Same units as target                   |
| MAE         | $\frac{1}{n}\sum                     | y_i - \hat{y}\_i                       | $   | Robust to outliers |
| R²          | $1 - \frac{SS_{res}}{SS_{tot}}$      | Proportion of variance explained (0-1) |
| Adjusted R² | $1 - \frac{(1-R^2)(n-1)}{n-d-1}$     | Penalizes unnecessary features         |

Where $SS_{res} = \sum(y_i - \hat{y}_i)^2$ and $SS_{tot} = \sum(y_i - \bar{y})^2$

## 8. Numerical Example

Given data points: (1, 2), (2, 3), (3, 5)

Using normal equation:

$\mathbf{X} = \begin{bmatrix}1 & 1 \\ 1 & 2 \\ 1 & 3\end{bmatrix}$, $\mathbf{y} = \begin{bmatrix}2 \\ 3 \\ 5\end{bmatrix}$

$\mathbf{X}^T\mathbf{X} = \begin{bmatrix}3 & 6 \\ 6 & 14\end{bmatrix}$

$(\mathbf{X}^T\mathbf{X})^{-1} = \frac{1}{6}\begin{bmatrix}14 & -6 \\ -6 & 3\end{bmatrix}$

$\mathbf{X}^T\mathbf{y} = \begin{bmatrix}10 \\ 26\end{bmatrix}$

$\mathbf{w} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y} = \begin{bmatrix}-0.33 \\ 1.5\end{bmatrix}$

Thus: $\hat{y} = 1.5x - 0.33$

MSE = $\frac{1}{3}[(2-1.17)^2 + (3-2.67)^2 + (5-4.17)^2]$ = 0.22

## 9. Python Implementation

```python
import numpy as np

class LinearRegression:
    def __init__(self, method='normal', alpha=0.01, iterations=1000):
        self.method = method
        self.alpha = alpha
        self.iterations = iterations
        self.weights = None

    def fit(self, X, y):
        n, d = X.shape
        # Add bias term
        X = np.column_stack([np.ones(n), X])

        if self.method == 'normal':
            self.weights = np.linalg.inv(X.T @ X) @ X.T @ y
        else:  # gradient descent
            self.weights = np.zeros(d + 1)
            for _ in range(self.iterations):
                predictions = X @ self.weights
                gradient = (2/n) * X.T @ (predictions - y)
                self.weights -= self.alpha * gradient

    def predict(self, X):
        n = X.shape[0]
        X = np.column_stack([np.ones(n), X])
        return X @ self.weights
```

## 10. Summary

Linear regression serves as the cornerstone of statistical modeling and machine learning. Its key aspects include:

1. **Mathematical Foundation**: The OLS method provides closed-form solutions through normal equations, while gradient descent offers scalability
2. **Statistical Inference**: Under standard assumptions, coefficients can be tested for significance with confidence intervals
3. **Regularization**: Ridge, Lasso, and Elastic Net address overfitting and multicollinearity
4. **Diagnostics**: Residual analysis validates model assumptions
5. **Interpretability**: Coefficients directly quantify feature effects on the target

Understanding linear regression provides essential foundations for advanced topics including logistic regression, generalized linear models, and neural networks.
