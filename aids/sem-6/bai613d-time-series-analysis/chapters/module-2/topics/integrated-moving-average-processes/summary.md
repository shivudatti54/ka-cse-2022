# Integrated Moving Average Processes

### Definition

- Integrated Moving Average (IMA) processes are a type of linear, nonstationary model in time series analysis
- They are a combination of Integrated Moving Average (IMA) and Autoregressive (AR) processes

### Key Points

- **Definition**: IMA process is defined as: φ(q)X(q) + θ(q)ε(q) = 0, where φ(q) and θ(q) are autoregressive and moving average polynomials, ε(q) is a white noise process, and X(q) is the lagged values of the time series
- **Properties**:
  - IMA processes are nonstationary and have a unit root
  - They are a special case of ARIMA processes
  - They are unstable and can be decomposed into two parts: an AR process and a MA process
- **Stationarity**: IMA processes are nonstationary and require differencing to become stationary
- **Forecasting**: IMA processes can be forecasted using ARIMA models with differencing

### Important Formulas

- **IMA process**: φ(q)X(q) + θ(q)ε(q) = 0
- **Differencing**: ΔX(q) = X(q) - X(q-1)
- **ARIMA model**: ARIMA(p, d, q) = φ(q)X(q) + θ(q)ε(q) + (1-L)^d X(q-d)

### Important Theorems

- **Unit Root Test**: Augmented Dickey-Fuller (ADF) test and KPSS test are used to test for unit roots in IMA processes
- **Stationarity Test**: KPSS test and PP test are used to test for stationarity in IMA processes

### Important Concepts

- **Autoregressive (AR) process**: A process where the current value is a function of past values
- **Moving Average (MA) process**: A process where the current value is a function of past errors
- **White Noise Process**: A process with constant variance and zero autocorrelation

### Revision Tips

- IMA processes are nonstationary and require differencing
- IMA processes can be forecasted using ARIMA models with differencing
- Unit root tests and stationarity tests are used to test for unit roots and stationarity in IMA processes
