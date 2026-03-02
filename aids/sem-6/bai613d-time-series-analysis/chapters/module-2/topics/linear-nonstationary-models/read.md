**Subject: Time Series Analysis**
**Module 2: Linear Nonstationary Models**

***

### **1. Introduction to Nonstationary Models**

In the previous module, we explored stationary time series models like AR, MA, and ARMA. A fundamental assumption of these models is that the series' mean and variance are constant over time (stationarity). However, real-world engineering data—such as stock prices, sensor readings from a degrading machine, or annual power consumption—often exhibit clear trends, cycles, or changing variability, making them **nonstationary**.

Linear Nonstationary Models extend the ARMA framework to handle this nonstationarity. The most common and powerful approach is to transform a nonstationary series into a stationary one through a technique called **differencing**. The resulting models are known as **Autoregressive Integrated Moving Average (ARIMA)** models.

***

### **2. Core Concepts: Differencing and the ARIMA Model**

#### **a) The Principle of Differencing**

The core idea is simple: if a time series has a trend, the *changes* between consecutive observations (the first differences) might be stationary.

*   Let the original series be `Y_t`.
*   The first difference is defined as: `∇Y_t = Y_t - Y_{t-1}`
*   If `∇Y_t` is stationary, we can model it using an ARMA model.
*   Sometimes, first differencing isn't enough. A **second difference** might be applied: `∇²Y_t = ∇(Y_t - Y_{t-1}) = (Y_t - Y_{t-1}) - (Y_{t-1} - Y_{t-2}) = Y_t - 2Y_{t-1} + Y_{t-2}`. This can remove quadratic trends.

The number of times we need to difference the series to achieve stationarity is denoted by the parameter **`d`** (the "I" or "Integrated" part in ARIMA).

#### **b) The ARIMA(p, d, q) Model**

An ARIMA model is formally defined by three order parameters:
*   **`p`**: The order of the Autoregressive (AR) part.
*   **`d`**: The degree of differencing (number of times the data was differenced to become stationary).
*   **`q`**: The order of the Moving Average (MA) part.

The general model is written as:
**ARIMA(p, d, q)**

**How it works:**
1.  Start with the nonstationary data `Y_t`.
2.  Difference it `d` times to create a new, stationary series `W_t`, where `W_t = ∇^d Y_t`.
3.  Model this new stationary series `W_t` as an ARMA(p, q) process.

The model equation for `W_t` is:
`W_t = c + φ₁W_{t-1} + ... + φ_pW_{t-p} + ε_t + θ₁ε_{t-1} + ... + θ_qε_{t-qi}`

Where `ε_t` is white noise.

**Example:** An ARIMA(1,1,1) model would be:
1.  `W_t = Y_t - Y_{t-1}` (because d=1)
2.  `W_t = φ₁W_{t-1} + ε_t + θ₁ε_{t-1}` (because p=1, q=1)

#### **c) Special Case: Random Walk Model**

A **Random Walk** is a simple but fundamental nonstationary model. It is an ARIMA(0,1,0) model. Its equation is:
`Y_t = Y_{t-1} + ε_t`

This means the value at time `t` is simply the previous value plus a random shock. It clearly has a stochastic trend and is nonstationary (its variance increases over time). It's often used as a baseline model for financial data or Brownian motion simulations.

#### **d) Identifying `d`: The Augmented Dickey-Fuller (ADF) Test**

How do we know what value of `d` to use? While looking at a time series plot for a trend is a good start, a formal statistical test is used: the **Augmented Dickey-Fuller (ADF) Test**.

*   **Null Hypothesis (H₀):** The time series *is* nonstationary (has a unit root).
*   **Alternative Hypothesis (H₁):** The time series *is* stationary.

You apply the test to the original series (`Y_t`).
*   If the **p-value > 0.05**, you **fail to reject H₀** and conclude the series is nonstationary. You then difference the series once (`∇Y_t`) and run the ADF test again.
*   If the **p-value ≤ 0.05**, you **reject H₀** and conclude the series is stationary. The number of times you differenced to get this result is your `d` value.

***

### **3. Example: Modeling Trendy Data**

Imagine you have sensor data `Y_t` measuring the wear on a bearing over time, showing a clear upward trend.

1.  **Plot & ADF Test:** The plot shows a trend. The ADF test on `Y_t` gives a high p-value (e.g., 0.8), confirming nonstationarity.
2.  **Differencing:** You calculate the first difference `W_t = Y_t - Y_{t-1}`. The plot of `W_t` now oscillates around a constant mean (no trend).
3.  **ADF Test Again:** The ADF test on `W_t` gives a low p-value (e.g., 0.01), confirming stationarity. Therefore, **`d = 1`**.
4.  **Model Identification:** You plot the ACF and PACF of the stationary series `W_t` to identify potential `p` and `q` orders.
5.  **Build ARIMA:** Suppose the ACF/PACF suggest an AR(1) model for `W_t`. You would then fit an **ARIMA(1,1,0)** model to the original data `Y_t`.

***

### **4. Key Points & Summary**

| Key Point | Description |
| :--- | :--- |
| **Purpose** | To model nonstationary time series data that exhibit trends. |
| **Core Technique** | **Differencing** (`∇^d Y_t`) is used to remove trends and achieve stationarity. |
| **Model** | **ARIMA(p, d, q)** models a series that has been differenced `d` times as an ARMA(p, q) process. |
| **Parameter `d`** | The order of integration. Found by iteratively applying the **ADF Test** until stationarity is achieved. |
| **Random Walk** | A special ARIMA(0,1,0) model where each step is a random shock, `Y_t = Y_{t-1} + ε_t`. |
| **Application** | Widely used in forecasting fields like signal processing, stock market analysis, and predictive maintenance. |

In summary, ARIMA models provide a structured, linear framework for analyzing and forecasting nonstationary time series by leveraging the power of differencing to reduce them to a well-understood stationary ARMA process.