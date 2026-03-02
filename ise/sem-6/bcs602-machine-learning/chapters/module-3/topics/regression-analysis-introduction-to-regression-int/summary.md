# Regression Analysis Revision Notes

### Introduction to Regression

- Regression analysis: a statistical method to establish a relationship between a dependent variable and one or more independent variables.
- Goal: to predict the value of the dependent variable based on the values of the independent variables.
- Assumptions:
  - Linearity
  - Independence
  - Homoscedasticity
  - Normality
  - No or little multicollinearity

### Introduction to Linear Regression

- Linear regression: a type of regression analysis where the relationship between the dependent variable and independent variable is modeled using a linear equation.
- Equation: y = β0 + β1x + ε
- Coefficients:
  - β0 (intercept)
  - β1 (slope)
  - ε (residual error)
- Formula: β1 = Σ[(xi - x̄)(yi - ȳ)] / Σ(xi - x̄)^2

### Multiple Linear Regression

- Multiple linear regression: a type of linear regression where the relationship between the dependent variable and multiple independent variables is modeled using a linear equation.
- Equation: y = β0 + β1x1 + β2x2 + ... + βNxN + ε
- Formula: β1 = Σ[(xi1 - x̄1)(yi - ȳ)] / Σ(xi1 - x̄1)^2
- β2 = ... = βN = ...

### Polynomial Regression

- Polynomial regression: a type of regression analysis where the relationship between the dependent variable and independent variable is modeled using a polynomial equation.
- Equation: y = β0 + β1x + β2x^2 + ... + βNx^N + ε
- Formula: β1 = Σ[(xi - x̄)(yi - ȳ)] / Σ(xi - x̄)^2
- β2 = ... = βN = ...

### Logistic Regression

- Logistic regression: a type of regression analysis where the relationship between the dependent variable and independent variable is modeled using a logistic equation.
- Equation: P(y = 1) = 1 / (1 + e^(-z)), where z = β0 + β1x + ε
- Formula: log(odds) = β0 + β1x
- Key concept: logistic function (Sigmoid function)

## Important Formulas

- Multiple Linear Regression: β = (X^T X)^-1 X^T Y
- Polynomial Regression: β = (X^T X)^-1 X^T Y
- Logistic Regression: log(odds) = β0 + β1x

## Important Definitions

- Residual error: ε = yi - (β0 + β1x + ...)
- Coefficient of determination (R-squared): measure of goodness of fit
- Standard error of the estimate: measure of variability of predicted values
