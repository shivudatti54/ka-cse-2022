# **Three Explicit Forms for the ARIMA Model**

## **Introduction**

The ARIMA (AutoRegressive Integrated Moving Average) model is a widely used statistical model for time series analysis. It is a powerful tool for forecasting and analyzing data that is subject to trends, seasonality, and random fluctuations. In this section, we will explore the three explicit forms of the ARIMA model, which are:

- ARIMA(p, d, q)
- ARIMA(p, d, q, s)
- ARIMA(p, d, q, s, r)

## **ARIMA(p, d, q)**

### Definition

The ARIMA(p, d, q) model is an autoregressive integrated moving average model with one differencing.

- **Autoregressive (AR)**: The model includes autoregressive terms that capture the relationships between past values of the time series.
- **Integrated (I)**: The model includes one differencing term to account for nonstationarity in the time series.
- **Moving Average (MA)**: The model includes moving average terms that capture the relationships between past errors (residuals) of the time series.
- p: The number of autoregressive terms.
- d: The degree of differencing.
- q: The number of moving average terms.

### Example

Suppose we have a time series data that is subject to a trend and seasonality, and we want to model it using the ARIMA(p, d, q) model. We can specify the model as follows:

ARIMA(2, 1, 1)

- p = 2: There are two autoregressive terms that capture the relationships between past values of the time series.
- d = 1: There is one differencing term to account for nonstationarity in the time series.
- q = 1: There is one moving average term that captures the relationships between past errors (residuals) of the time series.

### Key Concepts

- Autoregressive terms: Capture the relationships between past values of the time series.
- Differencing term: Accounts for nonstationarity in the time series.
- Moving average terms: Capture the relationships between past errors (residuals) of the time series.

## **ARIMA(p, d, q, s)**

### Definition

The ARIMA(p, d, q, s) model is an autoregressive integrated moving average model with one differencing and one seasonal differencing.

- **Autoregressive (AR)**: The model includes autoregressive terms that capture the relationships between past values of the time series.
- **Integrated (I)**: The model includes one differencing term to account for nonstationarity in the time series.
- **Moving Average (MA)**: The model includes moving average terms that capture the relationships between past errors (residuals) of the time series.
- **Seasonal differencing (s)**: The model includes one seasonal differencing term to account for nonstationarity in the time series due to seasonality.
- p: The number of autoregressive terms.
- d: The degree of differencing.
- q: The number of moving average terms.
- s: The seasonality parameter.

### Example

Suppose we have a time series data that is subject to a trend, seasonality, and irregular fluctuations, and we want to model it using the ARIMA(p, d, q, s) model. We can specify the model as follows:

ARIMA(2, 1, 1, 2)

- p = 2: There are two autoregressive terms that capture the relationships between past values of the time series.
- d = 1: There is one differencing term to account for nonstationarity in the time series.
- q = 1: There is one moving average term that captures the relationships between past errors (residuals) of the time series.
- s = 2: There are two seasonal differencing terms to account for nonstationarity in the time series due to seasonality.

### Key Concepts

- Autoregressive terms: Capture the relationships between past values of the time series.
- Differencing term: Accounts for nonstationarity in the time series.
- Moving average terms: Capture the relationships between past errors (residuals) of the time series.
- Seasonal differencing: Accounts for nonstationarity in the time series due to seasonality.

## **ARIMA(p, d, q, s, r)**

### Definition

The ARIMA(p, d, q, s, r) model is an autoregressive integrated moving average model with one differencing, one seasonal differencing, and one seasonally integrated component.

- **Autoregressive (AR)**: The model includes autoregressive terms that capture the relationships between past values of the time series.
- **Integrated (I)**: The model includes one differencing term to account for nonstationarity in the time series.
- **Moving Average (MA)**: The model includes moving average terms that capture the relationships between past errors (residuals) of the time series.
- **Seasonal differencing (s)**: The model includes one seasonal differencing term to account for nonstationarity in the time series due to seasonality.
- **Seasonally Integrated (r)**: The model includes one seasonally integrated component to account for nonstationarity in the time series due to seasonality.
- p: The number of autoregressive terms.
- d: The degree of differencing.
- q: The number of moving average terms.
- s: The seasonality parameter.
- r: The degree of seasonality.

### Example

Suppose we have a time series data that is subject to a trend, seasonality, irregular fluctuations, and periodic trends, and we want to model it using the ARIMA(p, d, q, s, r) model. We can specify the model as follows:

ARIMA(2, 2, 1, 3, 1)

- p = 2: There are two autoregressive terms that capture the relationships between past values of the time series.
- d = 2: There are two differencing terms to account for nonstationarity in the time series.
- q = 1: There is one moving average term that captures the relationships between past errors (residuals) of the time series.
- s = 3: There are three seasonal differencing terms to account for nonstationarity in the time series due to seasonality.
- r = 1: There is one seasonally integrated component to account for nonstationarity in the time series due to seasonality.

### Key Concepts

- Autoregressive terms: Capture the relationships between past values of the time series.
- Differencing term: Accounts for nonstationarity in the time series.
- Moving average terms: Capture the relationships between past errors (residuals) of the time series.
- Seasonal differencing: Accounts for nonstationarity in the time series due to seasonality.
- Seasonally integrated component: Accounts for nonstationarity in the time series due to seasonality.
