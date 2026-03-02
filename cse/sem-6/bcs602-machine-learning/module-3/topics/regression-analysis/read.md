# Module 3: Regression Analysis in Machine Learning

## 1. Introduction

Regression Analysis constitutes a fundamental paradigm within supervised machine learning, serving as the primary methodology for predicting continuous outcome variables from one or more predictor variables. Unlike classification tasks, which assign discrete categorical labels, regression quantifies relationships between variables to estimate numerical quantities. For engineering students at the B.Tech, MSc, and MCA levels, regression analysis is indispensable as it provides a rigorous mathematical framework for modeling relationships between variables—applications include predicting material strength from compositional data, estimating energy consumption from sensor readings, and forecasting system performance metrics.

The theoretical foundations of regression extend far beyond simple curve fitting; they encompass statistical inference, optimization theory, and linear algebra, making regression an essential cornerstone for understanding advanced machine learning methodologies.

---

## 2. Simple Linear Regression

### 2.1 Mathematical Formulation

Simple Linear Regression models the relationship between a single independent variable (feature) and a dependent variable (target) through a linear equation fitted to observed data points. The model assumes the following form:

**Model Equation:**
$$y = \beta_0 + \beta_1 x + \epsilon$$

Where:

- $y$: Dependent/Target variable (response)
- $x$: Independent/Feature variable (predictor)
- $\beta_0$: Y-intercept (bias term, also denoted as $\alpha$)
- $\beta_1$: Slope coefficient (regression coefficient, also denoted as $b$)
- $\epsilon$: Error term (residual), assumed to be normally distributed with mean zero and constant variance

**Interpretation:** The slope $\beta_1$ represents the expected change in the dependent variable for a one-unit increase in the independent variable. The intercept $\beta_0$ represents the expected value of $y$ when $x = 0$.

**Illustrative Example:** Consider predicting a student's examination grade ($y$) based on the number of study hours ($x$). The fitted equation $y = 50 + 5x$ indicates a baseline grade of 50 points when no study occurs, with an expected increase of 5 points for each additional hour studied.

### 2.2 Ordinary Least Squares (OLS) Estimation

The Ordinary Least Squares (OLS) method determines the optimal values of $\beta_0$ and $\beta_1$ by minimizing the sum of squared residuals (the vertical distances between observed and predicted values).

**Cost Function (Sum of Squared Errors):**
$$SSE(\beta_0, \beta_1) = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 = \sum_{i=1}^{n}(y_i - \beta_0 - \beta_1 x_i)^2$$

**Theorem (OLS Parameter Estimation):** The OLS estimators that minimize $SSE$ are given by:

$$\hat{\beta}_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2} = \frac{Cov(x,y)}{Var(x)}$$

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

Where $\bar{x}$ and $\bar{y}$ denote the sample means of $x$ and $y$ respectively.

**Proof of $\hat{\beta}_1$ Derivation:**

To find the minimizing values, we set the partial derivatives of $SSE$ with respect to $\beta_0$ and $\beta_1$ to zero:

$$\frac{\partial}{\partial \beta_0}SSE = -2\sum_{i=1}^{n}(y_i - \beta_0 - \beta_1 x_i) = 0$$
$$\frac{\partial}{\partial \beta_1}SSE = -2\sum_{i=1}^{n}x_i(y_i - \beta_0 - \beta_1 x_i) = 0$$

From the first equation:
$$\sum y_i = n\beta_0 + \beta_1 \sum x_i$$
$$\bar{y} = \beta_0 + \beta_1 \bar{x} \tag{1}$$

From the second equation:
$$\sum x_i y_i = \beta_0 \sum x_i + \beta_1 \sum x_i^2 \tag{2}$$

Substituting $\beta_0 = \bar{y} - \beta_1 \bar{x}$ from equation (1) into equation (2):
$$\sum x_i y_i = (\bar{y} - \beta_1 \bar{x})\sum x_i + \beta_1 \sum x_i^2$$
$$\sum x_i y_i = \bar{y}\sum x_i - \beta_1 \bar{x}\sum x_i + \beta_1 \sum x_i^2$$
$$\sum x_i y_i - \bar{y}\sum x_i = \beta_1 \left(\sum x_i^2 - \bar{x}\sum x_i\right)$$

Dividing by $n$:
$$\frac{1}{n}\sum x_i y_i - \bar{y}\bar{x} = \beta_1 \left(\frac{1}{n}\sum x_i^2 - \bar{x}^2\right)$$
$$\frac{1}{n}\sum (x_i - \bar{x})(y_i - \bar{y}) = \beta_1 \cdot \frac{1}{n}\sum (x_i - \bar{x})^2$$

Thus:
$$\hat{\beta}_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2} \quad \blacksquare$$

### 2.3 Gradient Descent Algorithm

While the closed-form OLS solution provides exact parameter estimates, Gradient Descent offers an iterative optimization approach essential for large-scale problems and neural networks.

**Algorithm:**

1. Initialize parameters $\beta_0, \beta_1$ randomly or to zero
2. Compute the gradient (partial derivatives) of the cost function
3. Update parameters: $\beta_j := \beta_j - \alpha \frac{\partial}{\partial \beta_j}J(\beta_0, \beta_1)$
4. Repeat until convergence

**For MSE Cost Function:**
$$\frac{\partial}{\partial \beta_0}MSE = -\frac{2}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)$$
$$\frac{\partial}{\partial \beta_1}MSE = -\frac{2}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)x_i$$

Where $\alpha$ (learning rate) controls the step size. Selection of $\alpha$ is critical: values too small yield slow convergence; values too large may cause divergence.

---

## 3. Multiple Linear Regression

### 3.1 Model Formulation

Real-world phenomena depend on multiple variables. Multiple Linear Regression extends the simple model to $p$ independent variables:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p + \epsilon$$

In matrix notation:
$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$$

Where:

- $\mathbf{y}$: $(n \times 1)$ vector of observations
- $\mathbf{X}$: $(n \times (p+1))$ design matrix with first column of ones
- $\boldsymbol{\beta}$: $((p+1) \times 1)$ vector of coefficients
- $\boldsymbol{\epsilon}$: $(n \times 1)$ vector of errors

### 3.2 Normal Equations (Closed-Form Solution)

The OLS solution in matrix form is obtained by solving the normal equations:

$$\mathbf{X}^T \mathbf{X} \boldsymbol{\beta} = \mathbf{X}^T \mathbf{y}$$

**Theorem:** The unique solution is given by:
$$\boldsymbol{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

**Proof:** Starting from the SSE in matrix form:
$$SSE = (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^T(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})$$

Differentiating with respect to $\boldsymbol{\beta}$ and setting to zero:
$$\frac{\partial}{\partial \boldsymbol{\beta}}SSE = -2\mathbf{X}^T(\mathbf{y} - \mathbf{X}\boldsymbol{\beta}) = 0$$
$$\mathbf{X}^T \mathbf{y} = \mathbf{X}^T \mathbf{X} \boldsymbol{\beta}$$
$$\boldsymbol{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} \quad \blacksquare$$

**Computational Note:** For large $p$, computing $(\mathbf{X}^T \mathbf{X})^{-1}$ is computationally expensive ($O(p^3)$). Gradient descent or regularization is preferred for high-dimensional problems.

---

## 4. Assumptions of Linear Regression (Gauss-Markov Theorem)

The validity of OLS inference depends on the following assumptions:

### 4.1 Gauss-Markov Assumptions

1. **Linearity:** The relationship between $X$ and $Y$ is linear: $Y = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$

2. **Independence:** Error terms are independent (no autocorrelation), particularly important for time-series data

3. **Homoscedasticity:** Error variance is constant: $Var(\epsilon_i) = \sigma^2$ for all $i$
   - **Violation:** Heteroscedasticity leads to inefficient estimates and invalid inference

4. **Normality:** Errors are normally distributed: $\epsilon_i \sim N(0, \sigma^2)$
   - Required for hypothesis testing and confidence intervals

5. **No Perfect Multicollinearity:** No independent variable is a perfect linear combination of others (rank($\mathbf{X}$) = $p+1$)

### 4.2 Diagnostic Tests

- **Residual Plots:** Plot residuals vs. fitted values to detect non-linearity and heteroscedasticity
- **Q-Q Plots:** Assess normality of residuals
- **Variance Inflation Factor (VIF):** Detect multicollinearity ($VIF_i = \frac{1}{1-R_i^2}$; VIF > 10 indicates problematic multicollinearity)
- **Durbin-Watson Test:** Detect autocorrelation in residuals

---

## 5. Model Evaluation Metrics

### 5.1 Error-Based Metrics

**Mean Absolute Error (MAE):**
$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

- Robust to outliers; measures average absolute deviation

**Mean Squared Error (MSE):**
$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

- Penalizes larger errors quadratically; sensitive to outliers

**Root Mean Squared Error (RMSE):**
$$RMSE = \sqrt{MSE}$$

- Interpretable in same units as $y$; preferred when large errors are particularly costly

### 5.2 Coefficient of Determination ($R^2$)

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

**Interpretation:** Proportion of variance in the dependent variable explained by the independent variables. Range: $[0, 1]$, where 1 indicates perfect prediction.

**Adjusted $R^2$:**
$$R_{adj}^2 = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

- Penalizes addition of irrelevant predictors; essential for multiple regression

### 5.3 Bias-Variance Trade-off

$$E[(y - \hat{y})^2] = \text{Bias}^2(\hat{y}) + \text{Var}(\hat{y}) + \sigma^2$$

- **High Bias (Underfitting):** Model is too simple, misses patterns
- **High Variance (Overfitting):** Model captures noise, fails to generalize

Cross-validation (k-fold) provides robust performance estimates by training on $k-1$ folds and validating on the remaining fold.

---

## 6. Advanced Regression Techniques

### 6.1 Polynomial Regression

When linear assumptions fail, polynomial features extend the model:
$$y = \beta_0 + \beta_1 x + \beta_2 x^2 + \cdots + \beta_d x^d + \epsilon$$

**Trade-off:** Higher degrees ($d$) reduce bias but increase variance and overfitting risk. Regularization addresses this.

### 6.2 Regularization

**Ridge Regression (L2 Regularization):**
$$\hat{\boldsymbol{\beta}}_{ridge} = \arg\min_{\boldsymbol{\beta}} \left\{ \sum_{i=1}^{n}(y_i - \mathbf{x}_i^T\boldsymbol{\beta})^2 + \lambda \sum_{j=1}^{p}\beta_j^2 \right\}$$

- Shrinks coefficients toward zero; effective for multicollinearity
- Solution: $\boldsymbol{\beta}_{ridge} = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$

**Lasso Regression (L1 Regularization):**
$$\hat{\boldsymbol{\beta}}_{lasso} = \arg\min_{\boldsymbol{\beta}} \left\{ \sum_{i=1}^{n}(y_i - \mathbf{x}_i^T\boldsymbol{\beta})^2 + \lambda \sum_{j=1}^{p}|\beta_j| \right\}$$

- Performs feature selection by driving some coefficients exactly to zero

---

## 7. Summary

Regression analysis provides a rigorous mathematical framework for predicting continuous numerical outcomes from input features. The fundamental objective is to determine the optimal parameters that minimize the discrepancy between predicted and actual values—quantified through cost functions such as Mean Squared Error. The Ordinary Least Squares method yields closed-form solutions under the Gauss-Markov assumptions, while Gradient Descent provides scalable iterative optimization. Multiple Linear Regression generalizes the framework to high-dimensional problems, though regularization techniques (Ridge, Lasso) become essential to mitigate overfitting and multicollinearity. Model evaluation employs multiple metrics—MAE, RMSE, and R²—alongside diagnostic procedures to validate underlying assumptions. Mastery of regression provides the foundational block for understanding regularization, classification (via logistic regression), and deep learning architectures, making it indispensable for engineering students pursuing data-driven methodologies.
