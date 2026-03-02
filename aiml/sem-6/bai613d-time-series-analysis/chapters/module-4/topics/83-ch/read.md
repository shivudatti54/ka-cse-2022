# **8.3 Ch: Checking the Stochastic Model**

## **Introduction**

In time series analysis, it is crucial to verify the adequacy of the selected stochastic model. This involves checking the model's assumptions, examining the residuals, and evaluating the model's performance. In this chapter, we will discuss the techniques for checking the stochastic model, including diagnostic tests, overfitting, and model evaluation.

## **Diagnostic Tests**

Diagnostic tests are used to check the model's assumptions and evaluate its performance. The following are some common diagnostic tests:

- **White Noise Test**: This test checks for the presence of white noise in the residuals. White noise is random and uncorrelated.
  - **Null Hypothesis**: The residuals are white noise.
  - **Alternative Hypothesis**: The residuals are not white noise.
- **Autocorrelation Function (ACF) Test**: This test checks for the presence of autocorrelation in the residuals. Autocorrelation occurs when the residuals are correlated with past values.
  - **Null Hypothesis**: The residuals are uncorrelated with past values.
  - **Alternative Hypothesis**: The residuals are correlated with past values.
- **Partial Autocorrelation Function (PACF) Test**: This test checks for the presence of partial autocorrelation in the residuals. Partial autocorrelation occurs when the residuals are correlated with distant past values.
  - **Null Hypothesis**: The residuals are uncorrelated with distant past values.
  - **Alternative Hypothesis**: The residuals are correlated with distant past values.

## **Overfitting**

Overfitting occurs when a model is too complex and fits the training data too well, resulting in poor performance on new, unseen data. Overfitting can be detected using the following methods:

- **Cross-Validation**: This method involves training and testing the model on separate subsets of the data.
- **Recursive Feature Elimination (RFE)**: This method involves recursively removing features until the model achieves optimal performance.
- **Regularization**: This method involves adding a penalty term to the loss function to reduce the model's complexity.

## **Model Evaluation**

Model evaluation involves assessing the model's performance and comparing it to other models. The following are some common metrics for model evaluation:

- **Mean Squared Error (MSE)**: This metric measures the average squared difference between the predicted and actual values.
- **Mean Absolute Error (MAE)**: This metric measures the average absolute difference between the predicted and actual values.
- **R-Squared (R²)**: This metric measures the proportion of the variance in the actual values that is explained by the predicted values.
- **Cross-Validation**: This method involves training and testing the model on separate subsets of the data to evaluate its performance.

## **Example**

Suppose we are analyzing a time series dataset using an ARIMA model. We can use the following code to perform diagnostic tests and evaluate the model's performance:

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset
data = pd.read_csv('data.csv')

# Perform diagnostic tests
white_noise_test = sm WhiteNoiseTest(data)
acf_test = sm.ACFTest(data)
pacf_test = sm.PACFTest(data)

# Evaluate the model's performance
mse = sm.OLS(data, model).fit().rsquared
mae = sm.OLS(data, model).fit().mean_absolute_error

print(white_noise_test.pvalue)
print(acf_test.pvalue)
print(pacf_test.pvalue)
print(mse)
print(mae)
```

This code performs diagnostic tests for white noise, autocorrelation, and partial autocorrelation, and evaluates the model's performance using MSE and MAE.
