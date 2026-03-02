# Multiple Linear Regression

## Introduction

Multiple linear regression extends simple linear regression to model the relationship between a dependent variable and **two or more** independent variables. It is one of the most widely used statistical and machine learning techniques for predictive modeling. While simple linear regression considers only one predictor, multiple linear regression captures the combined influence of multiple predictors on the response variable, enabling more accurate and realistic modeling of complex real-world phenomena.

## Mathematical Formulation

### Model Equation

The multiple linear regression model with _n_ independent variables is expressed as:

$$Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_nX_n + \varepsilon$$

Where:

- $Y$: dependent variable (response/target variable)
- $X_1, X_2, ..., X_n$: independent variables (predictors/features)
- $\beta_0$: population intercept (expected value of Y when all Xs are zero)
- $\beta_1, \beta_2, ..., \beta_n$: population regression coefficients (partial slopes)
- $\varepsilon$: error term (random disturbance)

The estimated model using sample data is:

$$\hat{Y} = b_0 + b_1X_1 + b_2X_2 + ... + b_nX_n$$

### Matrix Formulation

For computational efficiency and theoretical development, multiple regression is expressed in matrix form. Given _m_ observations:

$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$$

Where:

- $\mathbf{Y}$: $(m \times 1)$ response vector
- $\mathbf{X}$: $(m \times (n+1))$ design matrix with first column of ones for intercept
- $\boldsymbol{\beta}$: $((n+1) \times 1)$ coefficient vector $[\beta_0, \beta_1, ..., \beta_n]^T$
- $\boldsymbol{\varepsilon}$: $(m \times 1)$ error vector

## Derivation of OLS Estimator

### Objective Function

The Ordinary Least Squares (OLS) method minimizes the sum of squared residuals (RSS):

$$S(\boldsymbol{\beta}) = \sum_{i=1}^{m} \varepsilon_i^2 = \boldsymbol{\varepsilon}^T\boldsymbol{\varepsilon} = (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^T(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})$$

### Minimization Using Matrix Calculus

Taking the derivative with respect to $\boldsymbol{\beta}$ and setting to zero:

$$\frac{\partial S}{\partial \boldsymbol{\beta}} = -2\mathbf{X}^T(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}) = 0$$

This yields the **normal equations**:

$$\mathbf{X}^T\mathbf{X}\boldsymbol{\beta} = \mathbf{X}^T\mathbf{Y}$$

### Closed-Form Solution

Assuming $\mathbf{X}^T\mathbf{X}$ is invertible (no perfect multicollinearity), the OLS estimator is:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$$

This is the fundamental result of linear regression theory.

### Conditions for Validity

1. **Full rank condition**: $\mathbf{X}$ must have full column rank (rank = n+1)
2. **Invertibility**: $\mathbf{X}^T\mathbf{X}$ must be non-singular
3. **Sample size**: $m > n + 1$ (more observations than parameters)

## The Gauss-Markov Theorem

The Gauss-Markov theorem establishes the optimality properties of OLS:

**Theorem**: Under assumptions of linearity, homoscedasticity, independence, and no perfect multicollinearity, the OLS estimator $\hat{\boldsymbol{\beta}}$ is the **Best Linear Unbiased Estimator (BLUE)** of $\boldsymbol{\beta}$.

"Best" means minimum variance among all linear unbiased estimators. This justifies OLS as the optimal choice under standard conditions.

## Interpretation of Coefficients

Each coefficient $\beta_i$ represents the **partial effect** of $X_i$ on Y, holding all other variables constant (ceteris paribus):

$$\beta_i = \frac{\partial Y}{\partial X_i}$$

**Example**: In the model $\text{Salary} = 30000 + 5000(\text{Experience}) + 2000(\text{Education})$

- $\beta_1 = 5000$: Each additional year of experience increases salary by $5,000, holding education constant
- $\beta_2 = 2000$: Each additional year of education increases salary by $2,000, holding experience constant

This partial interpretation distinguishes multiple regression from simple regression.

## Assumptions (CLRM Assumptions)

### 1. Linearity

$Y = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ — The relationship between predictors and response is linear.

### 2. Random Sampling

Observations are independently and identically distributed (i.i.d.).

### 3. No Perfect Multicollinearity

$\text{rank}(\mathbf{X}) = n + 1$ — No predictor is a perfect linear combination of others.

### 4. Zero Conditional Mean

$E(\varepsilon|X) = 0$ — Error term has zero mean given the predictors.

### 5. Homoscedasticity

$\text{Var}(\varepsilon|X) = \sigma^2 \mathbf{I}$ — Constant variance of errors.

### 6. Normality (for inference)

$\varepsilon \sim N(0, \sigma^2 \mathbf{I})$ — Errors are normally distributed.

## Statistical Inference

### Coefficient Standard Errors

Under homoscedasticity, the variance-covariance matrix of $\hat{\boldsymbol{\beta}}$ is:

$$\text{Var}(\hat{\boldsymbol{\beta}}) = \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}$$

The estimated error variance is:

$$\hat{\sigma}^2 = \frac{\text{RSS}}{m - n - 1} = \frac{\sum(y_i - \hat{y}_i)^2}{m - n - 1}$$

The standard error of $b_j$ is $SE(b_j) = \sqrt{\hat{\sigma}^2 \cdot (\mathbf{X}^T\mathbf{X})^{-1}_{jj}}$

### t-Test for Individual Coefficients

For testing $H_0: \beta_j = 0$ against $H_1: \beta_j \neq 0$:

$$t_j = \frac{b_j - 0}{SE(b_j)}$$

Under $H_0$, $t_j \sim t_{m-n-1}$. Reject $H_0$ if $|t_j| > t_{\alpha/2, m-n-1}$ or p-value < $\alpha$.

### F-Test for Overall Significance

For testing $H_0: \beta_1 = \beta_2 = ... = \beta_n = 0$ against $H_1$: At least one $\beta_j \neq 0$:

$$F = \frac{(\text{SS}_{regression} / n)}{(\text{SS}_{residual} / (m - n - 1))} = \frac{MSR}{MSE}$$

Under $H_0$, $F \sim F_{n, m-n-1}$. Reject $H_0$ if $F > F_{\alpha, n, m-n-1}$.

### Confidence Intervals

A $(1-\alpha)\%$ confidence interval for $\beta_j$ is:

$$b_j \pm t_{\alpha/2, m-n-1} \cdot SE(b_j)$$

### Prediction Intervals

For a new observation $\mathbf{x}_0$, the prediction interval is:

$$\hat{y}_0 \pm t_{\alpha/2, m-n-1} \cdot \hat{\sigma}\sqrt{1 + \mathbf{x}_0^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_0}$$

## Multicollinearity

### Definition

Multicollinearity occurs when two or more independent variables are highly correlated, violating the no-perfect-multicollinearity assumption.

### Problems Caused

1. **Inflated standard errors**: Coefficient estimates become unstable
2. **Unstable estimates**: Small data changes cause large coefficient changes
3. **Contradictory signs**: Coefficients may have unexpected signs
4. **Statistical insignificance**: t-tests may fail to detect true effects

### Detection Methods

**Variance Inflation Factor (VIF)**:

$$\text{VIF}(X_j) = \frac{1}{1 - R_j^2}$$

Where $R_j^2$ is the R² from regressing $X_j$ on all other predictors.

| VIF Value    | Interpretation                             |
| ------------ | ------------------------------------------ |
| VIF = 1      | No correlation                             |
| 1 < VIF < 5  | Moderate correlation                       |
| 5 ≤ VIF < 10 | High correlation (concern)                 |
| VIF ≥ 10     | Severe multicollinearity (action required) |

**Condition Index**: $\sqrt{\lambda_{max}/\lambda_j}$ where $\lambda$ are eigenvalues of $\mathbf{X}^T\mathbf{X}$. Values > 30 indicate severe multicollinearity.

### Remediation Strategies

1. **Remove correlated predictors**: Drop one of highly correlated pairs
2. **Combine variables**: Use principal component analysis (PCA)
3. **Regularization**: Apply Ridge (L2) or Lasso (L1) regression
4. **Collect more data**: May reduce variance of estimates
5. **Variable transformation**: Create interaction terms or polynomial features

## Model Evaluation Metrics

### Coefficient of Determination (R²)

$$R^2 = 1 - \frac{SS_{residual}}{SS_{total}} = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

R² represents the proportion of variance in Y explained by all predictors. However, R² **always increases** (or stays same) when adding predictors, even irrelevant ones.

### Adjusted R²

$$\bar{R}^2 = 1 - \frac{(1 - R^2)(m - 1)}{m - n - 1}$$

Adjusted R² penalizes for adding unnecessary predictors. It can **decrease** if predictors do not improve the model. Preferred for model comparison.

### Akaike Information Criterion (AIC)

$$\text{AIC} = m \ln\left(\frac{\text{RSS}}{m}\right) + 2(n + 1)$$

### Bayesian Information Criterion (BIC)

$$\text{BIC} = m \ln\left(\frac{\text{RSS}}{m}\right) + (n + 1)\ln(m)$$

Lower AIC/BIC indicates better model. BIC penalizes model complexity more heavily than AIC.

## Residual Diagnostics

### Types of Residuals

1. **Ordinary residuals**: $e_i = y_i - \hat{y}_i$
2. **Standardized residuals**: $r_i = \frac{e_i}{\hat{\sigma}\sqrt{1 - h_{ii}}}$
3. **Studentized residuals**: $t_i = \frac{e_i}{\hat{\sigma}_{-i}\sqrt{1 - h_{ii}}}$

### Leverage (Hat Values)

$$h_{ii} = \mathbf{x}_i^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i$$

High leverage points ($h_{ii} > 2(n+1)/m$) have unusual predictor values.

### Cook's Distance

$$D_i = \frac{e_i^2}{n\hat{\sigma}^2} \cdot \frac{h_{ii}}{(1 - h_{ii})^2}$$

Measures influence of observation $i$ on all fitted values. $D_i > 4/m$ indicates influential points.

### Diagnostic Plots

1. **Residuals vs Fitted**: Check linearity and homoscedasticity
2. **Q-Q Plot**: Check normality of residuals
3. **Scale-Location Plot**: Check homoscedasticity
4. **Residuals vs Leverage**: Identify influential observations

## Feature Selection Methods

### 1. Forward Selection

1. Start with no predictors
2. Add the most significant variable (lowest p-value < threshold)
3. Repeat until no remaining variables are significant

### 2. Backward Elimination

1. Start with all predictors
2. Remove the least significant variable (highest p-value > threshold)
3. Repeat until all remaining variables are significant

### 3. Stepwise Selection

Combines forward and backward: variables can be added or removed at each step.

### 4. All Subset Regression

Evaluate all $2^n$ possible models and select based on R², Adjusted R², AIC, or BIC.

## Regularized Regression

### Ridge Regression (L2)

Minimizes: $\sum(y_i - \hat{y}_i)^2 + \lambda \sum b_j^2$

Shrinks coefficients toward zero, reducing variance at cost of slight bias.

### Lasso Regression (L1)

Minimizes: $\sum(y_i - \hat{y}_i)^2 + \lambda \sum |b_j|$

Shrinks some coefficients exactly to zero, performing variable selection.

### Elastic Net

Combines L1 and L2 penalties: $\sum(y_i - \hat{y}_i)^2 + \lambda_1 \sum |b_j| + \lambda_2 \sum b_j^2$

## Numerical Example

**Problem**: Given the following data for predicting house prices (Y in $1000s):

| Observation | Area (X₁) | Bedrooms (X₂) | Price (Y) |
| ----------- | --------- | ------------- | --------- |
| 1           | 1400      | 3             | 245       |
| 2           | 1600      | 3             | 312       |
| 3           | 1700      | 2             | 279       |
| 4           | 1875      | 4             | 308       |
| 5           | 1100      | 2             | 199       |

**Solution**: Using OLS formulas or software:

$$\hat{Y} = 48.23 + 0.12X_1 + 15.26X_2$$

**Interpretation**:

- Base price: $48,230 when Area = 0 and Bedrooms = 0
- Each sq ft adds $120 to price (holding bedrooms constant)
- Each bedroom adds $15,260 to price (holding area constant)

## Assessment Questions

### Question 1 (Hard - Computational)

Consider a multiple regression model with 3 predictors and 25 observations. The design matrix $\mathbf{X}$ has $\mathbf{X}^T\mathbf{X} = \begin{pmatrix} 25 & 100 & 50 \\ 100 & 500 & 200 \\ 50 & 200 & 100 \end{pmatrix}$ and $\mathbf{X}^T\mathbf{Y} = \begin{pmatrix} 200 \\ 900 \\ 400 \end{pmatrix}$. Calculate the OLS coefficient estimates $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$. What is the predicted value for an observation with X = (1, 10, 5)?

### Question 2 (Hard - Analytical)

In a regression model with VIF values of 2.1, 8.5, 1.3, and 15.2 for four predictors, which variable(s) should be addressed? Justify your response with statistical reasoning. If you decide to remove the problematic variable(s), recalculate the remaining VIFs assuming the removed variable explained 85% of the variance in one of the remaining predictors.

### Question 3 (Hard - Interpretation)

A researcher finds that adding a highly correlated predictor increases R² from 0.72 to 0.85 but decreases Adjusted R² from 0.68 to 0.61. Explain this phenomenon. Which model would you recommend and why?

### Question 4 (Hard - Application)

You are given residual sum of squares = 150 and total sum of squares = 800 for a model with 5 predictors and 30 observations. Calculate R², Adjusted R², and perform an F-test at α = 0.05. What conclusions can you draw about the model's significance?
