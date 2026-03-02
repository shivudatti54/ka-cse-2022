# Regression Analysis: Introduction to Regression

### Definition and Purpose

Regression analysis is a statistical method used to establish a relationship between a dependent variable (target variable) and one or more independent variables (predictor variables). The goal of regression analysis is to create a mathematical model that can predict the value of the dependent variable based on the values of the independent variables.

### Types of Regression Analysis

There are several types of regression analysis, including:

- **Linear Regression**: a simple linear relationship between the dependent and independent variables.
- **Multiple Linear Regression**: a linear relationship between the dependent variable and multiple independent variables.
- **Polynomial Regression**: a non-linear relationship between the dependent variable and one or more independent variables, where the relationship is modeled using a polynomial equation.
- **Logistic Regression**: a non-linear relationship between the dependent variable and one or more independent variables, where the relationship is modeled using a logistic function.

### Introduction to Linear Regression

Linear regression is a type of regression analysis that establishes a linear relationship between the dependent and independent variables. The general equation for linear regression is:

y = β0 + β1x + ε

where:

- y is the dependent variable
- x is the independent variable
- β0 is the intercept or constant term
- β1 is the slope coefficient
- ε is the error term

### Key Concepts of Linear Regression

- **Linearity**: the relationship between the dependent and independent variables is linear.
- **Assumptions**: the data should meet certain assumptions, such as linearity, independence, homoscedasticity, normality, and no multicollinearity.
- **Coefficients**: the slope coefficient (β1) and intercept coefficient (β0) are estimated using regression analysis.
- **Residuals**: the difference between the observed values and the predicted values.

### Example of Linear Regression

Suppose we want to predict the price of a house based on its size (in square feet). We collect data on the size of the house and its corresponding price, and use linear regression to create a model.

| Size (sq ft) | Price  |
| ------------ | ------ |
| 1000         | 200000 |
| 1200         | 250000 |
| 1500         | 300000 |

Using linear regression, we estimate the slope coefficient (β1) and intercept coefficient (β0). The model is:

Price = 200000 + 200x

where x is the size of the house in square feet.

### Introduction to Multiple Linear Regression

Multiple linear regression is a type of regression analysis that establishes a linear relationship between the dependent variable and multiple independent variables. The general equation for multiple linear regression is:

y = β0 + β1x1 + β2x2 + … + βnxn + ε

where:

- y is the dependent variable
- x1, x2, …, xn are the independent variables
- β0 is the intercept or constant term
- β1, β2, …, βn are the slope coefficients
- ε is the error term

### Key Concepts of Multiple Linear Regression

- **Multiple Linearity**: the relationship between the dependent and independent variables is linear, but with multiple independent variables.
- **Assumptions**: the data should meet certain assumptions, such as linearity, independence, homoscedasticity, normality, and no multicollinearity.
- **Coefficients**: the slope coefficients (β1, β2, …, βn) are estimated using regression analysis.
- **Residuals**: the difference between the observed values and the predicted values.

### Example of Multiple Linear Regression

Suppose we want to predict the price of a house based on its size (in square feet), number of bedrooms, and number of bathrooms. We collect data on the size of the house, number of bedrooms, number of bathrooms, and its corresponding price, and use multiple linear regression to create a model.

| Size (sq ft) | Bedrooms | Bathrooms | Price  |
| ------------ | -------- | --------- | ------ |
| 1000         | 2        | 1         | 200000 |
| 1200         | 3        | 2         | 250000 |
| 1500         | 4        | 3         | 300000 |

Using multiple linear regression, we estimate the slope coefficients (β1, β2, β3) and intercept coefficient (β0). The model is:

Price = 200000 + 100x + 500Bedrooms + 1000Bathrooms

where x is the size of the house in square feet, Bedrooms is the number of bedrooms, and Bathrooms is the number of bathrooms.

### Introduction to Polynomial Regression

Polynomial regression is a type of regression analysis that establishes a non-linear relationship between the dependent variable and one or more independent variables, where the relationship is modeled using a polynomial equation. The general equation for polynomial regression is:

y = β0 + β1x + β2x^2 + … + βnx^n + ε

where:

- y is the dependent variable
- x is the independent variable
- β0 is the intercept or constant term
- β1, β2, …, βn are the slope coefficients
- ε is the error term

### Key Concepts of Polynomial Regression

- **Non-Linearity**: the relationship between the dependent and independent variables is non-linear.
- **Assumptions**: the data should meet certain assumptions, such as linearity, independence, homoscedasticity, normality, and no multicollinearity.
- **Coefficients**: the slope coefficients (β1, β2, …, βn) are estimated using regression analysis.
- **Residuals**: the difference between the observed values and the predicted values.

### Example of Polynomial Regression

Suppose we want to predict the price of a house based on its size (in square feet). We collect data on the size of the house and its corresponding price, and use polynomial regression to create a model.

| Size (sq ft) | Price  |
| ------------ | ------ |
| 1000         | 200000 |
| 1200         | 250000 |
| 1500         | 300000 |

Using polynomial regression, we estimate the slope coefficients (β1, β2) and intercept coefficient (β0). The model is:

Price = 200000 + 100x + 10x^2

where x is the size of the house in square feet.

### Introduction to Logistic Regression

Logistic regression is a type of regression analysis that establishes a non-linear relationship between the dependent variable and one or more independent variables, where the relationship is modeled using a logistic function. The general equation for logistic regression is:

P(y=1) = 1 / (1 + e^(-β0 - β1x - … – βnx))

where:

- P(y=1) is the probability of the dependent variable being 1
- x is the independent variable
- β0 is the intercept or constant term
- β1, β2, …, βn are the slope coefficients
- e is the base of the natural logarithm

### Key Concepts of Logistic Regression

- **Non-Linearity**: the relationship between the dependent and independent variables is non-linear.
- **Assumptions**: the data should meet certain assumptions, such as linearity, independence, homoscedasticity, normality, and no multicollinearity.
- **Coefficients**: the slope coefficients (β1, β2, …, βn) are estimated using logistic regression.
- **Residuals**: the difference between the observed values and the predicted values.

### Example of Logistic Regression

Suppose we want to predict the probability of a person being insured based on their age and income. We collect data on the age and income of the person, and their corresponding insurance status, and use logistic regression to create a model.

| Age | Income | Insurance Status |
| --- | ------ | ---------------- |
| 25  | 40000  | Yes              |
| 30  | 50000  | No               |
| 35  | 60000  | Yes              |

Using logistic regression, we estimate the slope coefficients (β1, β2) and intercept coefficient (β0). The model is:

P(Insurance) = 1 / (1 + e^(-β0 - 0.1Age + 0.01Income))

where Age is the age of the person, and Income is the income of the person.
