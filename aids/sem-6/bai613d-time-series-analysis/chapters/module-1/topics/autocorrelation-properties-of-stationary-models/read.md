# Autocorrelation Properties of Stationary Models

## Introduction

In Time Series Analysis, understanding the internal structure of a data series is paramount. For **stationary models**, which have constant statistical properties over time, the **autocorrelation function (ACF)** serves as a fundamental tool. It quantifies the linear relationship between a time series and a lagged version of itself, essentially revealing the "memory" of the process. This module explores the core properties of autocorrelation for stationary models, which are crucial for model identification, estimation, and diagnostics.

## Core Concepts

### 1. Definition of Autocorrelation

The autocorrelation coefficient measures the correlation between observations at different time points. For a stationary time series $\{Z_t\}$ with constant mean $\mu$ and variance $\sigma^2$, the autocorrelation between times $t$ and $t+k$ is defined as the correlation between $Z_t$ and $Z_{t+k}$.

The autocovariance function at lag $k$ is:
$$\gamma_k = \text{Cov}(Z_t, Z_{t+k}) = E[(Z_t - \mu)(Z_{t+k} - \mu)]$$

The autocorrelation function (ACF) at lag $k$ is then defined by normalizing the autocovariance:
$$\rho_k = \frac{\gamma_k}{\gamma_0} = \frac{\text{Cov}(Z_t, Z_{t+k})}{\text{Var}(Z_t)}$$
where $\gamma_0 = \sigma^2$ is the variance of the process. By definition, $\rho_0 = 1$.

### 2. Key Properties for *Any* Stationary Process

For any stationary process, the ACF possesses two fundamental mathematical properties:

*   **Symmetry:** $\rho_k = \rho_{-k}$
    The correlation of a $k$-step lag is identical to the correlation of a $k$-step lead. The ACF is an even function.

*   **Bounds:** $-1 \leq \rho_k \leq 1$
    The value of any autocorrelation coefficient must lie between -1 and +1, inclusive.

### 3. Autocorrelation Patterns of Common Stationary Models

Different models have distinct theoretical ACF patterns, which are like fingerprints used for identification.

#### a) White Noise Process
A white noise process $\{a_t\}$ is a sequence of uncorrelated, identically distributed random variables with mean zero and constant variance $\sigma_a^2$.
*   **Theoretical ACF:**
    $\rho_0 = 1$
    $\rho_k = 0$ **for all $k \neq 0$**
*   **Interpretation:** There is no discernible linear relationship between any two points separated by a lag. The process has no memory.

#### b) First-Order Autoregressive Process - AR(1)
An AR(1) model is defined as $Z_t = \phi_1 Z_{t-1} + a_t$, where $|\phi_1| < 1$ for stationarity.
*   **Theoretical ACF:**
    $\rho_k = \phi_1^k$ **for $k = 0, 1, 2, ...$**
*   **Interpretation:** The ACF decays **exponentially** towards zero. If $\phi_1 > 0$ (positive autocorrelation), it decays slowly in a positive direction. If $\phi_1 < 0$ (negative autocorrelation), it alternates in sign while the magnitude decays exponentially.

**Example:** For an AR(1) model with $\phi_1 = 0.7$:
$\rho_0 = 1$
$\rho_1 = 0.7^1 = 0.7$
$\rho_2 = 0.7^2 = 0.49$
$\rho_3 = 0.7^3 \approx 0.34$
...and so on.

#### c) First-Order Moving Average Process - MA(1)
An MA(1) model is defined as $Z_t = a_t - \theta_1 a_{t-1}$, where $a_t$ is white noise.
*   **Theoretical ACF:**
    $\rho_0 = 1$
    $\rho_1 = \frac{-\theta_1}{1 + \theta_1^2}$
    $\rho_k = 0$ **for all $k \geq 2$**
*   **Interpretation:** The ACF has a sharp **cut-off** after lag 1. This signifies that the process only has a memory of one time period.

**Example:** For an MA(1) model with $\theta_1 = -0.5$:
$\rho_1 = \frac{-(-0.5)}{1 + (-0.5)^2} = \frac{0.5}{1.25} = 0.4$
$\rho_2 = 0$, $\rho_3 = 0$, etc.

### 4. The Correlogram

The correlogram is the primary graphical tool for analyzing autocorrelation. It is a bar chart of the **sample autocorrelation function** ($r_k$) plotted against the lag $k$. By comparing the sample ACF from our data to the theoretical ACFs of known models, we can identify a suitable model for our time series.

## Key Points & Summary

*   **Purpose:** The Autocorrelation Function (ACF) is the key tool for identifying patterns and dependencies within a stationary time series.
*   **Universal Properties:** For any stationary process, the ACF is symmetric ($\rho_k = \rho_{-k}$) and bounded ($|\rho_k| \leq 1$).
*   **Model Fingerprints:**
    *   **White Noise:** ACF is zero for all lags $k \geq 1$.
    *   **AR(p) Models:** ACF decays exponentially or sinusoidally; it **tails off**.
    *   **MA(q) Models:** ACF has a sharp **cut-off** after lag $q$.
*   **Application:** Analyzing the sample ACF (correlogram) of a dataset allows an engineer to propose an appropriate model (e.g., AR, MA) and its order, which is the first critical step in the Box-Jenkins methodology for time series forecasting. This is essential for predicting trends in engineering data like sensor readings, network traffic, or power demand.