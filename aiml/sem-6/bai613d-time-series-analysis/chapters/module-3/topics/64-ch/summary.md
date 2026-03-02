# **6.4 Ch: Time Series Analysis**

## **Objectives of Identification**

- Identify the underlying model for a given time series data
- Determine the number of parameters to be estimated
- Develop a strategy for model selection and evaluation

## **Identification Techniques**

- **Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF)**
  - ACF: measures correlation between time series and lagged values
  - PACF: measures correlation between time series and lagged values, controlling for intermediate lags
- **Cross-Correlation Function (CCF)**
  - measures correlation between two different time series
- **Maximum Likelihood Estimation (MLE)**
  - estimates model parameters by maximizing likelihood function

## **Important Formulas and Definitions**

- **Autocorrelation Coefficient (ρ)**
  - measures correlation between time series and lagged values
  - defined as: ρ(t) = cov(X(t), X(t-h)) / (σ^2 \* var(X(t-h)))
- **Partial Autocorrelation Coefficient (φ)**
  - measures correlation between time series and lagged values, controlling for intermediate lags
  - defined as: φ(k) = cov(X(t), X(t-h)) / var(X(t-h))
- **Serial Correlation Coefficient (S)**
  - measures serial correlation in time series
  - defined as: S = ρ(1) / (1 - ρ(1))

## **Theorems and Concepts**

- **Strong Stationarity**
  - a time series is strong stationary if its mean and variance are constant, and its autocorrelation function decays to zero as lag increases
- **Weak Stationarity**
  - a time series is weak stationary if its mean and variance are constant, but its autocorrelation function does not decay to zero as lag increases

## **Quick Revision Tips**

- Understand the different identification techniques and their applications
- Be able to calculate and interpret autocorrelation coefficients, partial autocorrelation coefficients, and serial correlation coefficients
- Familiarize yourself with the concepts of strong and weak stationarity
