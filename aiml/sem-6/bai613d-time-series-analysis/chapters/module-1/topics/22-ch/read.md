# **2.2 Ch: Autocorrelation Function and Spectrum**

## **Introduction**

In time series analysis, the autocorrelation function (ACF) is a crucial tool for understanding the relationship between different time periods in a time series. It measures the correlation between a time series and a lagged version of itself. In this section, we will explore the concept of autocorrelation function and its applications.

## **Definition**

The autocorrelation function (ACF) is defined as the correlation between a time series X(t) and a lagged version of itself, denoted as X(t-k), where k is the lag.

ACF(X(t), X(t-k)) = Cov(X(t), X(t-k)) / (σ_X^2 \* σ_X^2)

where Cov(X(t), X(t-k)) is the covariance between X(t) and X(t-k), and σ_X^2 is the variance of X(t).

## **Types of Autocorrelation**

There are several types of autocorrelation, including:

- **Autocorrelation at zero lag**: This is the correlation between a time series and itself.
- **Partial autocorrelation**: This is the correlation between a time series and a lagged version of itself, while controlling for other lags.
- **Spectral density**: This is the power spectral density of a time series, which represents the distribution of power across different frequencies.

## **Properties of Autocorrelation Function**

The autocorrelation function has several important properties, including:

- **Symmetry**: The ACF is symmetric around the zero lag.
- **Stationarity**: The ACF is a function of lag and is constant over time.
- **Unbiasedness**: The ACF is unbiased estimator of the true autocovariance.

## **Example**

Suppose we have a time series X(t) with values 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. We can calculate the ACF of X(t) using the following formula:

ACF(X(t), X(t-k)) = Cov(X(t), X(t-k)) / (σ_X^2 \* σ_X^2)

| Lag (k) | ACF(X(t), X(t-k)) |
| ------- | ----------------- |
| 0       | 1                 |
| 1       | 0.5               |
| 2       | -0.2              |
| 3       | -0.5              |
| 4       | 0.2               |

In this example, we can see that the ACF is symmetric around the zero lag and decreases as the lag increases.

## **Applications of Autocorrelation Function**

The autocorrelation function has several important applications in time series analysis, including:

- **Time series forecasting**: The ACF can be used to identify patterns and trends in a time series, which can be used to make predictions.
- **Filtering and smoothing**: The ACF can be used to filter and smooth a time series by removing noise and identifying trends.
- **Spectral analysis**: The ACF can be used to analyze the power spectral density of a time series, which can be used to identify frequencies and patterns.
