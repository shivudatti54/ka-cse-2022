# Regression Evaluation Metrics
## Introduction

Regression is a fundamental task in machine learning, where the goal is to predict a continuous output variable based on one or more input features. Evaluating the performance of a regression model is crucial to understand its strengths and weaknesses. In this topic, we will discuss various metrics used to evaluate the performance of regression models.

Regression evaluation metrics provide a way to measure the difference between the predicted and actual values of the target variable. These metrics help us to understand how well the model is performing and identify areas where it can be improved. In this topic, we will cover the most commonly used regression evaluation metrics, including Mean Squared Error (MSE), Mean Absolute Error (MAE), Coefficient of Determination (R-squared), and Mean Absolute Percentage Error (MAPE).

## Key Concepts

### 1. Mean Squared Error (MSE)

The Mean Squared Error (MSE) is one of the most widely used metrics for evaluating regression models. It calculates the average squared difference between the predicted and actual values of the target variable. The MSE is calculated using the following formula:

MSE = (1/n) \* Σ(yi - yi')^2

where yi is the actual value, yi' is the predicted value, and n is the total number of observations.

### 2. Mean Absolute Error (MAE)

The Mean Absolute Error (MAE) is another popular metric for evaluating regression models. It calculates the average absolute difference between the predicted and actual values of the target variable. The MAE is calculated using the following formula:

MAE = (1/n) \* Σ|yi - yi'|

where yi is the actual value, yi' is the predicted value, and n is the total number of observations.

### 3. Coefficient of Determination (R-squared)

The Coefficient of Determination (R-squared) is a metric that measures the proportion of the variance in the target variable that is explained by the predictor variables. The R-squared value ranges from 0 to 1, where a higher value indicates a better fit of the model to the data. The R-squared is calculated using the following formula:

R-squared = 1 - (SSE / SST)

where SSE is the sum of the squared errors, and SST is the total sum of squares.

### 4. Mean Absolute Percentage Error (MAPE)

The Mean Absolute Percentage Error (MAPE) is a metric that calculates the average absolute percentage difference between the predicted and actual values of the target variable. The MAPE is calculated using the following formula:

MAPE = (1/n) \* Σ|(yi - yi') / yi| \* 100

where yi is the actual value, yi' is the predicted value, and n is the total number of observations.

## Examples

### Example 1: Calculating MSE and MAE

Suppose we have a regression model that predicts the house prices based on the number of bedrooms. The actual and predicted values are as follows:

| Actual Value | Predicted Value |
| --- | --- |
| 200000 | 220000 |
| 250000 | 240000 |
| 300000 | 280000 |
| 350000 | 320000 |

Calculate the MSE and MAE for this model.

Solution:

MSE = (1/4) \* Σ(yi - yi')^2
= (1/4) \* [(200000 - 220000)^2 + (250000 - 240000)^2 + (300000 - 280000)^2 + (350000 - 320000)^2]
= 1500000

MAE = (1/4) \* Σ|yi - yi'|
= (1/4) \* [|200000 - 220000| + |250000 - 240000| + |300000 - 280000| + |350000 - 320000|]
= 12500

### Example 2: Calculating R-squared

Suppose we have a regression model that predicts the stock prices based on the historical data. The actual and predicted values are as follows:

| Actual Value | Predicted Value |
| --- | --- |
| 100 | 120 |
| 120 | 110 |
| 150 | 140 |
| 180 | 160 |

Calculate the R-squared value for this model.

Solution:

SSE = Σ(yi - yi')^2
= [(100 - 120)^2 + (120 - 110)^2 + (150 - 140)^2 + (180 - 160)^2]
= 2000

SST = Σ(yi - y')^2
= [(100 - 120)^2 + (120 - 110)^2 + (150 - 140)^2 + (180 - 160)^2]
= 5000

R-squared = 1 - (SSE / SST)
= 1 - (2000 / 5000)
= 0.6

## Exam Tips

1. Understand the formulas for calculating MSE, MAE, R-squared, and MAPE.
2. Be able to interpret the results of these metrics, including identifying the strengths and weaknesses of a regression model.
3. Know how to calculate the R-squared value using the SSE and SST.
4. Understand the limitations of each metric, including the sensitivity to outliers and the assumption of normality.
5. Be able to compare the performance of different regression models using these metrics.
6. Understand the importance of evaluating the performance of a regression model using multiple metrics.
7. Know how to use these metrics to identify areas for improvement in a regression model.