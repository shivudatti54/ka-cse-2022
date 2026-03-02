# Regression Analysis: Quick Revision Notes

### Introduction to Regression

- **Regression Analysis**: Statistical method to establish a relationship between two or more variables.
- **Definition**: Regression equation: y = f(x), where y is the response variable and x is the predictor variable.
- **Objective**: To predict the value of y based on the value of x.

### Introduction to Linear Regression

- **Linear Regression**: A special case of regression analysis where the relationship between y and x is linear and continuous.
- **Linear Regression Equation**: y = β0 + β1x + ε, where β0 is the intercept, β1 is the slope, and ε is the error term.
- **Assumptions**:
  - Linearity
  - Independence
  - Homoscedasticity
  - Normality
  - No multicollinearity

### Multiple Linear Regression

- **Multiple Linear Regression**: A type of linear regression where multiple predictor variables are used to predict the response variable.
- **Regression Equation**: y = β0 + β1x1 + β2x2 + … + βnxn + ε, where β0 is the intercept, β1, β2, …, βn are the coefficients, and ε is the error term.
- **Assumptions**:
  - Linearity
  - Independence
  - Homoscedasticity
  - Normality
  - No multicollinearity

### Polynomial Regression

- **Polynomial Regression**: A type of regression analysis where the relationship between y and x is non-linear and can be represented by a polynomial equation.
- **Regression Equation**: y = β0 + β1x + … + βnxn + ε, where β0, β1, …, βn are the coefficients, and ε is the error term.
- **Assumptions**:
  - Linearity
  - Independence
  - Homoscedasticity
  - Normality
  - No multicollinearity

### Logistic Regression

- **Logistic Regression**: A type of regression analysis used for binary classification problems, where the response variable is binary (0 or 1).
- **Regression Equation**: P(y=1) = 1 / (1 + e^(-z)), where z = β0 + β1x + … + βnxn, and ε is the error term.
- **Assumptions**:
  - Independence
  - Homoscedasticity
  - Log-normality

Important Formulas and Theorems:

- **Ordinary Least Squares (OLS)**: The method used to estimate the coefficients in linear regression.
- **Multiple Correlation Coefficient (R)**: Measures the strength of the relationship between multiple predictor variables and the response variable.
- **F-Statistic**: Used to test the significance of the coefficients in multiple linear regression.
- **Log-Likelihood Ratio Test**: Used to test the significance of the model in logistic regression.
