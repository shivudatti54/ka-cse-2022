# Three Explicit Forms for the ARIMA Model

### TIME SERIES ANALYSIS

#### Key Concepts:

- ARIMA model: Autoregressive Integrated Moving Average process
- Autoregressive (AR) model: emphasis on past values
- Integrated (I) model: differencing to make time series stationary
- Moving Average (MA) model: emphasis on past errors

#### Important Formulas and Definitions:

- ARIMA(p, d, q) model:
  - p: number of autoregressive terms
  - d: degree of differencing
  - q: number of moving average terms
- Autocorrelation Function (ACF):
  - measures correlation between series at different lags
- Partial Autocorrelation Function (PACF):
  - measures correlation between series and errors at different lags

#### Theorems:

- **Autocovariance Stationarity Theorem**:
  - ARIMA model is stationary if and only if the autocovariance function converges to zero as the lag increases
- **Orthogonality Theorem**:
  - ARIMA model is orthogonal if and only if the partial autocovariance function converges to zero as the lag increases

#### Important Formulas:

- **ARIMA(p, d, q) model equation**:
  - y*t = φ1y*{t-1} + φ2y*{t-2} + ... + φpy*{t-p} + θ1ε*{t-1} + θ2ε*{t-2} + ... + θqe\_{t-q}
  - where y_t is the time series value, φ_i are AR coefficients, θ_j are MA coefficients, ε_t is the error term, and d is the degree of differencing

#### Quick Revision Tips:

- Understand the role of AR, I, and MA terms in the ARIMA model
- Know the formulas for ACF and PACF
- Recall the theorems related to stationarity and orthogonality
- Be able to write the ARIMA model equation with its parameters
