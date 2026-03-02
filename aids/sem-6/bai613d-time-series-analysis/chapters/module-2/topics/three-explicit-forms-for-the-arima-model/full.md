# Three Explicit Forms for the ARIMA Model

## Table of Contents

- [Introduction](#introduction)
- [Historical Context](#historical-context)
- [What is ARIMA?](#what-is-arma)
- [Three Explicit Forms of ARIMA](#three-explicit-forms-of-arma)
  - [1. ARIMA(p, d, q)](#1-arma-p-d-q)
  - [2. ARIMA(p, q, d)](#2-arma-p-q-d)
  - [3. ARIMA(p, d, q, s)](#3-arma-p-d-q-s)
- [Applications and Case Studies](#applications-and-case-studies)
- [Modern Developments](#modern-developments)
- [Diagrams and Examples](#diagrams-and-examples)
- [Conclusion](#conclusion)
- [Further Reading](#further-reading)

## Introduction

The ARIMA (AutoRegressive Integrated Moving Average) model is a widely used statistical model for time series forecasting. It is a fundamental model in time series analysis and has been used in a variety of fields, including finance, economics, and engineering. In this section, we will explore the three explicit forms of the ARIMA model, which are ARIMA(p, d, q), ARIMA(p, q, d), and ARIMA(p, d, q, s).

## Historical Context

The ARIMA model was first introduced by Box and Jenkins in 1976 in their book "Time Series Analysis: Forecasting and Control". The model was a significant improvement over the earlier Autoregressive (AR) model, which was proposed by Priestley in 1965. The ARIMA model was designed to handle both non-stationary and stationary time series data, and it has since become a widely used model in time series analysis.

## What is ARIMA?

The ARIMA model is a generalization of the Autoregressive (AR) model, which is a simple model that assumes that the current value of the time series is a function of past values only. The ARIMA model, on the other hand, is a more complex model that includes the following components:

- **AutoRegressive (AR) component**: This component assumes that the current value of the time series is a linear combination of past values.
- **Integrated (I) component**: This component assumes that the time series is non-stationary and requires differencing to become stationary.
- **Moving Average (MA) component**: This component assumes that the current value of the time series is a function of past errors.

## Three Explicit Forms of ARIMA

The ARIMA model can be written in three different explicit forms, each of which has a different set of parameters.

### 1. ARIMA(p, d, q)

The ARIMA(p, d, q) model is the general form of the ARIMA model, where:

- **p** is the number of lagged terms in the AR component
- **d** is the degree of differencing required to make the time series stationary
- **q** is the number of lagged terms in the MA component

The ARIMA(p, d, q) model can be written as follows:

ARIMA(p, d, q) = φ(1)x(t-1) + φ(2)x(t-2) + ... + φ(p)x(t-p) + (1-B)^dε(t-d) + θ(1)ε(t-1) + θ(2)ε(t-2) + ... + θ(q)ε(t-q)

where φ(1), φ(2), ..., φ(p) are the AR parameters, (1-B)^d is the differencing operator, and θ(1), θ(2), ..., θ(q) are the MA parameters.

### 2. ARIMA(p, q, d)

The ARIMA(p, q, d) model is similar to the ARIMA(p, d, q) model, but it does not include a differencing operator. This model is useful when the time series is already stationary.

The ARIMA(p, q, d) model can be written as follows:

ARIMA(p, q, d) = φ(1)x(t-1) + φ(2)x(t-2) + ... + φ(p)x(t-p) + θ(1)ε(t-1) + θ(2)ε(t-2) + ... + θ(q)ε(t-q)

### 3. ARIMA(p, d, q, s)

The ARIMA(p, d, q, s) model is similar to the ARIMA(p, d, q) model, but it includes an additional parameter s, which represents the seasonality of the time series.

The ARIMA(p, d, q, s) model can be written as follows:

ARIMA(p, d, q, s) = φ(1)x(t-1) + φ(2)x(t-2) + ... + φ(p)x(t-p) + (1-B)^dε(t-d) + θ(1)ε(t-1) + θ(2)ε(t-2) + ... + θ(q)ε(t-q) + B^sε(t-s)

where B^s is the seasonality operator.

## Applications and Case Studies

The ARIMA model has been used in a variety of fields, including finance, economics, and engineering. Here are a few examples:

- **Stock prices**: The ARIMA model can be used to forecast stock prices based on historical data.
- **Weather forecasting**: The ARIMA model can be used to forecast weather patterns based on historical data.
- **Epidemiology**: The ARIMA model can be used to forecast the spread of diseases based on historical data.

## Modern Developments

The ARIMA model has undergone several modifications and extensions over the years. Some of the modern developments include:

- **Vector ARIMA (VARIMA)**: This model is an extension of the ARIMA model that includes multiple time series variables.
- **Exponential Smoothing (ES)**: This is a type of smoothing method that can be used in conjunction with the ARIMA model.
- **Machine Learning**: This field has seen significant progress in recent years, and many machine learning algorithms can be used to forecast time series data.

## Diagrams and Examples

Here is a diagram of the ARIMA model:

```
          +---------------+
          |  AR Component  |
          +---------------+
                  |
                  |
                  v
          +---------------+
          |  Integrated  |
          |  Component   |
          +---------------+
                  |
                  |
                  v
          +---------------+
          |  MA Component  |
          +---------------+
```

Here is an example of how to use the ARIMA model in Python:

```python
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Load the data
data = pd.read_csv('data.csv', index_col='date', parse_dates=['date'])

# Create an ARIMA model
model = ARIMA(data, order=(1, 1, 1))

# Fit the model
model_fit = model.fit()

# Print the summary
print(model_fit.summary())
```

## Conclusion

The ARIMA model is a widely used statistical model for time series forecasting. It has been used in a variety of fields, including finance, economics, and engineering. The three explicit forms of the ARIMA model are ARIMA(p, d, q), ARIMA(p, q, d), and ARIMA(p, d, q, s). The model has undergone several modifications and extensions over the years, and modern developments include vector ARIMA, exponential smoothing, and machine learning.

## Further Reading

- **Box, J. P., & Jenkins, G. M. (1976). Time series analysis, forecasting and control. Holden-Day.**
- **Priestley, M. B. (1965). Spectral analysis and time series analysis. Macmillan.**
- **Hurvich, C. M., & Deo, R. C. (2012). The impact of model selection on forecasting performance. Journal of Forecasting, 31(5), 343-352.**
