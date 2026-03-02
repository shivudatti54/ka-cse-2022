# Multiple Linear Regression

## Introduction

Multiple Linear Regression (MLR) is a statistical technique used to model the relationship between a dependent variable and one or more independent variables. It is an extension of simple linear regression, where we have more than one predictor variable. In MLR, we try to find the best-fitting linear equation that predicts the value of the dependent variable based on the values of the independent variables.

Multiple Linear Regression is a widely used technique in machine learning and data analysis, as it allows us to analyze the relationship between multiple variables and make predictions based on that analysis. It has numerous applications in various fields, including business, economics, social sciences, and healthcare.

## Key Concepts

### Assumptions of Multiple Linear Regression

For MLR to be applicable, certain assumptions must be met:

1. **Linearity**: The relationship between the dependent variable and the independent variables should be linear.
2. **Independence**: Each observation should be independent of the others.
3. **Homoscedasticity**: The variance of the residuals should be constant across all levels of the independent variables.
4. **Normality**: The residuals should be normally distributed.
5. **No multicollinearity**: The independent variables should not be highly correlated with each other.

### Coefficients and Intercept

In MLR, we have a coefficient (β) for each independent variable, which represents the change in the dependent variable for a one-unit change in the independent variable, while holding all other independent variables constant. We also have an intercept (α) that represents the value of the dependent variable when all independent variables are equal to zero.

### Ordinary Least Squares (OLS) Method

The OLS method is used to estimate the coefficients and intercept of the MLR model. The goal of OLS is to minimize the sum of the squared residuals between the observed values and the predicted values.

### Coefficient of Determination (R-squared)

R-squared measures the proportion of the variance in the dependent variable that is explained by the independent variables. It ranges from 0 to 1, where a higher value indicates a better fit of the model.

## Examples

### Example 1: Predicting House Prices

Suppose we want to predict the price of a house based on its size, number of bedrooms, and location. We collect data on these variables and use MLR to estimate the coefficients and intercept.

| Size (sqft) | Bedrooms | Location | Price ($) |
| --- | --- | --- | --- |
| 1000 | 2 | City | 200000 |
| 1500 | 3 | Suburbs | 300000 |
| 2000 | 4 | City | 400000 |
| ... | ... | ... | ... |

Using OLS, we estimate the coefficients and intercept:

Price = 100000 + 50(Size) + 20000(Bedrooms) - 10000(Location)

### Example 2: Predicting Stock Prices

Suppose we want to predict the price of a stock based on its dividend yield, price-to-earnings ratio, and moving average. We collect data on these variables and use MLR to estimate the coefficients and intercept.

| Dividend Yield | P/E Ratio | Moving Average | Price ($) |
| --- | --- | --- | --- |
| 0.05 | 20 | 50 | 100 |
| 0.03 | 15 | 40 | 80 |
| 0.07 | 25 | 60 | 120 |
| ... | ... | ... | ... |

Using OLS, we estimate the coefficients and intercept:

Price = 50 + 10(Dividend Yield) + 5(P/E Ratio) + 2(Moving Average)

## Exam Tips

1. Make sure to check the assumptions of MLR before applying the technique.
2. Use the OLS method to estimate the coefficients and intercept.
3. Interpret the coefficients and intercept in the context of the problem.
4. Use R-squared to evaluate the goodness of fit of the model.
5. Be aware of the limitations of MLR, such as multicollinearity and non-linearity.
6. Use techniques such as regularization to address multicollinearity.
7. Consider using alternative techniques, such as decision trees or random forests, if the data is non-linear.