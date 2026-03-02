# Autocorrelation Properties of Stationary Models

## Introduction

In the study of Time Series Analysis, understanding the internal structure and dependencies within a data series is paramount. For **stationary time series**—those whose statistical properties like mean and variance are constant over time—the autocorrelation function (ACF) serves as a fundamental tool. It quantifies the linear relationship between a time series and a lagged version of itself, providing crucial insights into the underlying process that generated the data. This module explores the autocorrelation properties of standard stationary models, namely the Autoregressive (AR), Moving Average (MA), and Autoregressive Moving Average (ARMA) models.

## Core Concepts

### 1. Autocorrelation Function (ACF)

The autocorrelation coefficient at lag *k*, denoted as ρₖ, measures the correlation between observations *k* time periods apart. It is defined as:

**ρₖ = Covariance(Yₜ, Yₜ₋ₖ) / Variance(Yₜ) = γₖ / γ₀**

where:
*   *γₖ* is the autocovariance at lag *k*.
*   *γ₀* is the variance of the process.

The plot of ρₖ against *k* (the lag) is called the **correlogram** and is the primary visual tool for identifying the nature of a stationary process.

### 2. Properties of Stationary Models

Stationary models have ACFs with distinct characteristics that help in model identification.

#### a) Moving Average (MA) Model

An MA(q) model is defined as:
**Yₜ = μ + εₜ + θ₁εₜ₋₁ + θ₂εₜ₋₂ + ... + θ_qεₜ₋_q**
where *εₜ* is white noise (a sequence of uncorrelated random variables with zero mean and constant variance).

*   **ACF Property:** The autocorrelation for an MA(q) model **cuts off** abruptly after lag *q*. This means:
    *   ρₖ is significant for *k = 1, 2, ..., q*.
    *   ρₖ ≈ 0 for all lags *k > q*.
*   **Why?** The process depends only on the last *q+1* random shocks. Once the lag exceeds the order of the model, there is no direct dependency, so the theoretical correlation is zero.
*   **Example:** For an MA(2) model like `Yₜ = εₜ + 0.5εₜ₋₁ - 0.3εₜ₋₂`, the ACF will have significant spikes at lags 1 and 2 and will be approximately zero for all lags *k ≥ 3*.

#### b) Autoregressive (AR) Model

An AR(p) model is defined as:
**Yₜ = c + φ₁Yₜ₋₁ + φ₂Yₜ₋₂ + ... + φ_pYₜ₋_p + εₜ**

*   **ACF Property:** The autocorrelation for an AR(p) model **tails off** or decays gradually towards zero. It often exhibits a mixture of exponential decay and damped sine waves. It does not cut off abruptly.
*   **Why?** A current observation is directly correlated with its immediate predecessor, which is correlated with its own predecessor, and so on. This creates a chain reaction of dependency that propagates indefinitely, though its strength diminishes with time.
*   **Example:** For a stationary AR(1) model (`Yₜ = φYₜ₋₁ + εₜ`), the ACF is given by ρₖ = φᵏ. If φ = 0.8, the ACF decays exponentially: ρ₁=0.8, ρ₂=0.64, ρ₃=0.512, and so on.

#### c) Autoregressive Moving Average (ARMA) Model

An ARMA(p, q) model combines both AR and MA components:
**Yₜ = c + φ₁Yₜ₋₁ + ... + φ_pYₜ₋_p + εₜ + θ₁εₜ₋₁ + ... + θ_qεₜ₋_q**

*   **ACF Property:** The ACF of an ARMA model **tails off** after the first *q-p* lags. Its behavior is dominated by the AR component in the long run. The initial few lags are influenced by both the AR and MA terms, but for larger lags, the decay pattern mirrors that of a pure AR process.
*   **Why?** The MA component affects the short-term dependencies (the first *q* lags), while the AR component governs the long-term persistence and the overall decay pattern.

## Partial Autocorrelation Function (PACF)

To complement the ACF and uniquely identify models, we use the **Partial Autocorrelation Function (PACF)**, denoted as φₖₖ. The PACF measures the correlation between Yₜ and Yₜ₋ₖ after removing the effects of the intermediate lags (Yₜ₋₁, Yₜ₋₂, ..., Yₜ₋ₖ₋₁).

*   **AR(p) Model:** The PACF **cuts off** after lag *p*. This is a key identifier.
*   **MA(q) Model:** The PACF **tails off**.
*   **ARMA(p, q) Model:** The PACF tails off.

## Summary of Key Properties

| Model Type | Autocorrelation Function (ACF) | Partial Autocorrelation Function (PACF) |
| :--- | :--- | :--- |
| **AR(p)** | **Tails off** (exponential decay/sinusoidal) | **Cuts off** after lag *p* |
| **MA(q)** | **Cuts off** after lag *q* | **Tails off** |
| **ARMA(p, q)** | **Tails off** after lag *q-p* | **Tails off** |

## Key Points / Summary

*   The **Autocorrelation Function (ACF)** is a critical tool for identifying the nature of a stationary time series process.
*   **MA models** are characterized by an ACF that has a sharp **cut-off** after the model's order (*q*). This indicates that the process has a finite memory.
*   **AR models** are characterized by an ACF that **tails off** gradually and a PACF that **cuts off** after the model's order (*p*). This indicates a longer, decaying memory.
*   **ARMA models** exhibit a tailing-off ACF, with the initial pattern being influenced by both AR and MA components.
*   In practice, we compare the **sample ACF/PACF** (calculated from observed data) to these theoretical properties to select an appropriate model (e.g., if the sample ACF cuts off at lag 2, an MA(2) model is a likely candidate).
*   Always remember that these properties hold **only for stationary series**. Non-stationary data must be transformed (e.g., by differencing) before applying this analysis.