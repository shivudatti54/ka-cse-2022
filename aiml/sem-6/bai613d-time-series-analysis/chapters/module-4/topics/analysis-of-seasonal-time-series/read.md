Of course. Here is a comprehensive educational note on the analysis of seasonal time series, tailored for  engineering students.

***

# Module 4: Analysis of Seasonal Time Series

## 1. Introduction

In many real-world engineering and scientific applications, time series data exhibits patterns that repeat over fixed intervals. For instance, power consumption peaks every evening, river flow rates are highest during the monsoon season, and retail sales surge during festive periods. A **seasonal time series** is one that contains such a systematic, calendar-related component. The "season" can be any fixed period: daily (24 hours), weekly (7 days), monthly (12 months), or quarterly (4 quarters). The primary goal of seasonal time series analysis is to identify, model, and account for these regular periodic movements to better understand the underlying structure of the data and improve forecasts.

## 2. Core Concepts

### a) What is Seasonality?
Seasonality is a component of a time series that repeats at regular intervals. It is driven by factors like weather, customs, or calendar events. Crucially, it must have a **fixed and known period**. This distinguishes it from a cyclical pattern, which has a fluctuating, often unpredictable period (e.g., economic business cycles).

### b) The Additive and Multiplicative Models
To decompose a time series (`Y_t`), we assume it is composed of three components: Trend (`T_t`), Seasonality (`S_t`), and an irregular/random component (`I_t`). The relationship between these components is typically described by one of two models:

*   **Additive Model:** `Y_t = T_t + S_t + I_t`
    *   **Use Case:** When the magnitude of the seasonal fluctuations is **constant** throughout the series, regardless of the trend. The seasonality does not grow with the overall level of the series.
    *   **Example:** The variation in monthly average temperature in Bangalore. The difference between summer and winter temperatures is roughly the same year after year, even if the overall annual average is slowly increasing.

*   **Multiplicative Model:** `Y_t = T_t * S_t * I_t`
    *   **Use Case:** When the magnitude of the seasonal fluctuations **varies with the level** of the series. The seasonal effect is proportional to the trend.
    *   **Example:** The sales of a popular beverage. The "peak" during summer will be much higher if the brand's overall popularity is growing (a rising trend), and the "trough" in winter will be less severe. The seasonal effect is amplified by the trend.

**Note:** A multiplicative model can often be transformed into an additive one by taking the logarithm: `log(Y_t) = log(T_t) + log(S_t) + log(I_t)`.

### c) Seasonal Differencing
This is a crucial technique for making a seasonal time series stationary (i.e., removing the seasonal pattern). If a series has a seasonal period `s`, then **seasonal differencing** is performed by calculating the difference between an observation and the observation from the same point in the previous season.

*   **Formula:** `∇_s Y_t = Y_t - Y_{t-s}`
*   **Example:** For monthly data (`s=12`), the seasonal difference for March 2023 would be: `March 2023 - March 2022`.
*   **Application:** This is a key step in the **Seasonal ARIMA (SARIMA)** model, denoted as `ARIMA(p, d, q)(P, D, Q)s`, where `D` is the order of seasonal differencing and `s` is the seasonal period.

### d) Autocorrelation Function (ACF) and Seasonal Lags
The ACF plot is a powerful tool for detecting seasonality. In a seasonal series, the ACF will show significant spikes at the **seasonal lags** (i.e., at lag `s`, `2s`, `3s`, etc.), in addition to the gradual decay typical of non-seasonal ARMA processes.

*   **Example:** In monthly electricity demand data (`s=12`), you would expect to see a large positive autocorrelation at lag 12, a smaller one at lag 24, and so on. This indicates that the value this month is strongly correlated with the value from the same month last year.

## 3. Example: Decomposing a Series

Let's consider a hypothetical dataset of quarterly sales (in lakhs of units) for an AC manufacturing company in India.

| Quarter | Sales (Y_t) |
| :------ | :---------- |
| Q1 2022 | 15          |
| Q2 2022 | 45          |
| Q3 2022 | 60          |
| Q4 2022 | 20          |
| Q1 2023 | 18          |
| Q2 2023 | 50          |
| Q3 2023 | 65          |
| Q4 2023 | 22          |

**Observation:**
1.  The data shows a clear seasonal pattern: high sales in Q2 and Q3 (summer), and low sales in Q1 and Q4.
2.  The sales in 2023 are slightly higher than in 2022, indicating a possible upward **trend**.
3.  Since the peaks and troughs are increasing slightly, a **multiplicative model** might be appropriate. We could `log-transform` the data and then use a moving average method to estimate the trend (`T_t`).
4.  Once the trend is estimated, we can calculate the **seasonal indices** for each quarter (e.g., Q1 might have an index of 0.7, meaning sales in Q1 are typically 30% below the trend level).

## 4. Summary & Key Points

*   **Seasonality** is a periodic, repeating pattern in a time series with a fixed, known period (`s`).
*   Two primary models exist: **Additive** (constant seasonal swing) and **Multiplicative** (swing proportional to trend).
*   **Seasonal Differencing** (`Y_t - Y_{t-s}`) is a standard technique to remove seasonal non-stationarity.
*   The **ACF plot** is essential for visually identifying seasonality through significant spikes at lags `s`, `2s`, `3s`, etc.
*   Understanding seasonality is the first step towards building advanced forecasting models like **SARIMA**, which combine both non-seasonal and seasonal elements.