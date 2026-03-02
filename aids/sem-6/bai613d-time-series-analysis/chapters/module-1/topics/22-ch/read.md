# 2.2 Ch: Autocorrelation Function and Spectrum

=====================================================

## Introduction

---

In time series analysis, the autocorrelation function (ACF) is a fundamental concept used to measure the correlation between different time lags of a time series. It helps us understand how the series depends on its past values. In this section, we will explore the definition, interpretation, and calculation of the ACF.

## Definition and Interpretation

---

The autocorrelation function is a measure of the correlation between two time series values that are spaced a certain number of time units apart. Mathematically, it is defined as:

### Formula:

ρ(h) = (∑(x[t] \* x[t-h])) / (∑x[t]^2)

where:

- x[t] represents the value of the time series at time t
- h is the time lag (i.e., the number of time units between the two time series values)
- ρ(h) is the autocorrelation coefficient at time lag h
- ϑ represents the mean of the time series

The ACF is used to determine whether a time series is stationary or non-stationary. A stationary time series has an ACF that decays rapidly to zero, indicating that the series does not depend on its past values. On the other hand, a non-stationary time series has an ACF that decays slowly to zero or remains constant, indicating that the series depends on its past values.

## Calculation of ACF

---

The ACF can be calculated using the following steps:

1. Calculate the mean of the time series (θ).
2. Calculate the sum of the product of each pair of time series values at different time lags (i.e., ∑(x[t] \* x[t-h])).
3. Calculate the sum of the squares of each time series value (i.e., ∑x[t]^2).
4. Calculate the autocorrelation coefficient (ρ(h)) using the formula above.

### Example:

Suppose we have a time series with the following values:

| Time | Value |
| ---- | ----- |
| 1    | 2     |
| 2    | 3     |
| 3    | 4     |
| 4    | 5     |
| 5    | 6     |

To calculate the ACF, we first calculate the mean of the time series (θ = 3.6).

Next, we calculate the sum of the product of each pair of time series values at different time lags:

- ρ(0) = ∑(x[t] _ x[t]) = (2 _ 2) + (3 _ 3) + (4 _ 4) + (5 _ 5) + (6 _ 6) = 34
- ρ(1) = ∑(x[t] _ x[t-1]) = (2 _ 3) + (3 _ 4) + (4 _ 5) + (5 \* 6) = 30
- ρ(2) = ∑(x[t] _ x[t-2]) = (3 _ 4) + (4 _ 5) + (5 _ 6) = 26
- ρ(3) = ∑(x[t] _ x[t-3]) = (4 _ 5) + (5 \* 6) = 22

Next, we calculate the sum of the squares of each time series value:

- ∑x[t]^2 = 2^2 + 3^2 + 4^2 + 5^2 + 6^2 = 38

Finally, we calculate the autocorrelation coefficient (ρ(h)) using the formula above:

- ρ(0) = 34 / 38 ≈ 0.895
- ρ(1) = 30 / 38 ≈ 0.789
- ρ(2) = 26 / 38 ≈ 0.684
- ρ(3) = 22 / 38 ≈ 0.579

## Autocorrelation Function and Spectrum

---

The autocorrelation function is related to the power spectral density (PSD) through the Fourier transform. The PSD is a measure of the power contained in each frequency band of the time series.

### Formula:

PSD = |X(e^jω)|^2

where:

- X(e^jω) represents the discrete Fourier transform of the time series
- ω is the angular frequency

The PSD can be used to identify the frequency bands present in the time series. For example, a time series with a high PSD in the frequency band corresponding to the dominant frequency component of the signal (e.g., 10 Hz) indicates that the signal has a strong periodic component.

## Key Concepts

---

- Autocorrelation function (ACF): a measure of the correlation between different time lags of a time series
- Autocorrelation coefficient (ρ(h)): the value of the ACF at time lag h
- Power spectral density (PSD): a measure of the power contained in each frequency band of the time series
- Fourier transform: a mathematical operation used to transform a time series into the frequency domain

### Example Use Cases:

- Identifying periodic components in a signal
- Determining the presence of noise in a signal
- Estimating the parameters of a time series model

By understanding the autocorrelation function and spectrum, you can gain insights into the properties of a time series and make informed decisions about its analysis and modeling.
