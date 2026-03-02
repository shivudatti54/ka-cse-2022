# **Three Explicit Forms for the ARIMA Model**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Autoregressive (AR) Model](#autoregressive-ar-model)
3. [Moving Average (MA) Model](#moving-average-ma-model)
4. [Integrated (I) Model](#integrated-i-model)
5. [ARIMA Model with Three Explicit Forms](#arima-model-with-three-explicit-forms)

## **Introduction**

The ARIMA (AutoRegressive Integrated Moving Average) model is a widely used statistical model for time series forecasting. The model combines three key components: Autoregressive (AR), Moving Average (MA), and Integrated (I). In this study material, we will explore the three explicit forms of the ARIMA model.

## **Autoregressive (AR) Model**

The Autoregressive (AR) model is used to capture the autocorrelation in the data. It assumes that the current value of the time series is a function of past values.

- Definition: AR(p) model - The model has a p-order where the current value is a linear combination of p past values with coefficients.
- Example: AR(1) model - The current value is a linear combination of the past value with a coefficient.

## **Moving Average (MA) Model**

The Moving Average (MA) model is used to capture the autocorrelation in the errors.

- Definition: MA(q) model - The model has a q-order where the current error is a linear combination of q errors in the past.
- Example: MA(1) model - The current error is a linear combination of the past error with a coefficient.

## **Integrated (I) Model**

The Integrated (I) model is used to capture the non-stationarity in the data.

- Definition: I(d) model - The model has a d-order where the differences between consecutive values are used to make the time series stationary.
- Example: I(1) model - The differences between consecutive values are used to make the time series stationary.

## **ARIMA Model with Three Explicit Forms**

The ARIMA model can be represented in three explicit forms:

### 1. ARIMA(p, d, q)

- Definition: The model has an AR(p) component, an I(d) component, and an MA(q) component.
- Example: ARIMA(2, 1, 1) model - The model has an AR(2) component with 2 past values, an I(1) component with the differences between consecutive values, and an MA(1) component with 1 past error.

### 2. ARIMA(p, q, d)

- Definition: The model has an AR(p) component, an MA(q) component, and an I(d) component.
- Example: ARIMA(1, 1, 2) model - The model has an AR(1) component with 1 past value, an MA(2) component with 2 past errors, and an I(1) component with the differences between consecutive values.

### 3. ARIMA(p, d, q)

- Definition: The model has an AR(p) component, an I(d) component, and an MA(q) component.
- Example: ARIMA(3, 2, 0) model - The model has an AR(3) component with 3 past values, an I(2) component with the differences between consecutive values, and no MA component.

## Key Concepts

- Autoregressive (AR) model
- Moving Average (MA) model
- Integrated (I) model
- ARIMA model with three explicit forms (ARIMA(p, d, q), ARIMA(p, q, d), ARIMA(p, d, q))

## Examples

- A company reports quarterly sales data. The ARIMA model can be used to forecast future sales.
- A time series analyst uses the ARIMA model to model the stock prices of a company.
- A meteorologist uses the ARIMA model to forecast weather patterns.

## Practice Problems

1.  Define the ARIMA model and its three explicit forms.
2.  Explain the role of each component in the ARIMA model.
3.  Provide examples of how the ARIMA model can be used in real-world applications.

By understanding the three explicit forms of the ARIMA model, you can effectively apply the model to various time series analysis problems and improve your forecasting accuracy.
