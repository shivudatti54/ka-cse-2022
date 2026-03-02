### 6.4 Ch: Time Series Analysis

#### Key Points

- **Objectives of Identification:**
  - Identify the underlying model for a given time series
  - Choose the appropriate model for forecast or analysis
- **Identification Techniques:**
  - Autocorrelation Function (ACF)
  - Partial Autocorrelation Function (PACF)
  - Cross-Correlation Function (CCF)
  - Transfer Function
  - Vector Autoregression (VAR)
- **Important Formulas:**

- Autocorrelation Function (ACF):
  - $\rho(k) = \frac{\text{Cov}(X_t, X_{t-k})}{\text{Var}(X_t)}$
- Partial Autocorrelation Function (PACF):
  - $\phi_{p}(k) = \frac{\text{Cov}(X_t, X_{t-k})}{\text{Cov}(X_t, X_{t-k-p})}$
- Quasi-Differencing:
  - $\Delta X_t = X_t - X_{t-1}$
- Moving Average (MA) Model:
  - $\phi B X_t = \theta B \varepsilon_t$
- Autoregressive (AR) Model:
  - $\theta B X_t = \varepsilon_t$
- Vector Autoregression (VAR) Model:
  - $\Phi B X_t = \varepsilon_t$

#### Important Definitions:

- **Autocorrelation**: The correlation between a time series and a lagged version of itself.
- **Partial Autocorrelation**: The correlation between a time series and a lagged version of itself, after removing the effects of intermediate lags.
- **Transfer Function**: A model that represents the relationship between a time series and another time series.
- **Vector Autoregression (VAR)**: A model that represents the relationship between multiple time series.

#### Important Theorems:

- **Durbin-Watson Test**: A statistical test used to detect autocorrelation in time series data.
- **Breusch-Godfrey Test**: A statistical test used to detect autocorrelation in time series data.
