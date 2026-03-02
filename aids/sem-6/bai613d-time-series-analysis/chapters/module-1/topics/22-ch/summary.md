# **2.2 Ch: Autocorrelation Function and Spectrum**

### Key Points

- **Autocorrelation Function (ACF):**
  - Definition: Measure of correlation between a time series at different lags.
  - Formula: ρ(τ) = ∑[x(t) \* x(t+τ)] / (∑[x(t) \* x(t)] \* ∑[x(t+τ) \* x(t+τ)])
  - Purpose: Identify patterns and dependencies in a time series.
- **Partial Autocorrelation Function (PACF):**
  - Definition: Measure of correlation between a time series at different lags, controlling for intermediate lags.
  - Formula: φ(k) = ρ(k) - ∑[ρ(i) \* φ(i)] for i = 0 to k-1
  - Purpose: Identify the order of an Autoregressive (AR) process.
- **Autoregressive (AR) Process:**
  - Definition: A time series model where the current value is a linear combination of past values.
  - Formula: x(t) = ∑[α(i) \* x(t-i)] + ε(t)
  - Purpose: Model dependence in a time series.
- **Moving Average (MA) Process:**
  - Definition: A time series model where the current value is a linear combination of past errors.
  - Formula: x(t) = ∑[β(j) \* ε(t-j)] + μ
  - Purpose: Model randomness in a time series.
- **Autocovariance Function:**
  - Definition: Measure of dispersion of a time series at different lags.
  - Formula: γ(τ) = E[(x(t) - μ) \* (x(t+τ) - μ)]
  - Purpose: Identify the autocovariance structure of a time series.

### Important Formulas and Theorems

- **Autocorrelation Function (ACF) Theorem:** The ACF converges to zero as the lag increases.
- **Moving Average (MA) Theorem:** The MA process has a constant variance if the errors are uncorrelated.
- **Yule-Walker Equations:** A set of equations used to estimate the parameters of an AR process.

### Key Concepts

- **Stationarity:** A time series is considered stationary if its mean and autocovariance structure are constant over time.
- **Non-stationarity:** A time series is considered non-stationary if its mean or autocovariance structure changes over time.

### Revision Tips

- Practice calculating the ACF and PACF for different time series.
- Understand the difference between AR and MA processes.
- Familiarize yourself with the Yule-Walker Equations and their application in estimating AR process parameters.
