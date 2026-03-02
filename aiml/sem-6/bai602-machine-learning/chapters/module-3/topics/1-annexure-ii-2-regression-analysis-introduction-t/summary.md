# Regression Analysis Revision Notes

### Introduction to Regression

- **Definition:** Regression analysis is a statistical method used to establish a relationship between a dependent variable (y) and one or more independent variables (x).
- **Purpose:** To predict the value of the dependent variable based on the values of the independent variable(s).
- **Types of Regression:** Polynomial, Multiple Linear, Non-Linear, Logistic Regression

### Introduction to Linear Regression

- **Definition:** Linear Regression is a type of regression analysis where the relationship between the independent variable(s) and the dependent variable is assumed to be linear.
- **Equation:** y = β0 + β1x + ε (where y is the dependent variable, x is the independent variable, β0 is the intercept, β1 is the slope, and ε is the error term)
- **Assumptions:**
  - Linearity
  - Independence
  - Homoscedasticity
  - Normality

### Multiple Linear Regression

- **Definition:** Multiple Linear Regression is a type of linear regression analysis where more than one independent variable is used to predict the dependent variable.
- **Equation:** y = β0 + β1x1 + β2x2 + … + βnxn + ε (where y is the dependent variable, x1, x2, …, xn are the independent variables, β0, β1, β2, …, βn are the coefficients, and ε is the error term)
- **Assumptions:**
  - Linearity
  - Independence
  - Homoscedasticity
  - Normality

### Polynomial Regression

- **Definition:** Polynomial Regression is a type of regression analysis where the relationship between the independent variable(s) and the dependent variable is assumed to be non-linear and can be represented by a polynomial equation.
- **Equation:** y = β0 + β1x + β2x^2 + … + βnx^n + ε (where y is the dependent variable, x is the independent variable, β0, β1, β2, …, βn are the coefficients, and ε is the error term)
- **Assumptions:**
  - No linear term is required (i.e., x^1 is required)
  - The relationship is non-linear but can be represented by a polynomial equation

## Formulas and Theorems

- **Ordinary Least Squares (OLS) Estimator:** β̂ = (X^T X)^-1 X^T y (where β̂ is the estimated coefficient, X is the design matrix, and y is the dependent variable)
- **Coefficient of Determination (R-squared):** R^2 = 1 - (SSE / SST) (where R^2 is the coefficient of determination, SSE is the sum of squared errors, and SST is the total sum of squares)
- **Residuals:** e_i = y_i - (β0 + β1x_i + … + βnx_n) (where e_i is the residual, y_i is the observed value, and β0, β1, …, βn are the estimated coefficients)
