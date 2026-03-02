# Calculating Forecasts and Probability Limits in Time Series Analysis

## Introduction

In Module 2 of Time Series Analysis, we transition from identifying models (like AR, MA, ARMA) to using them for their ultimate purpose: **forecasting**. A point forecast alone is insufficient; we must also quantify its uncertainty. This is achieved by calculating **Probability Limits** (often called prediction intervals). This lecture will guide you through the process of calculating forecasts and their associated probability limits for a standard ARMA model.

## Core Concepts

### 1. The Principle of Forecasting

The goal is to predict a future value $z_{l}$ ($l$ is the lead time) based on the current and past observations up to time $t$ ($z_t, z_{t-1}, z_{t-2}, ...$). The best forecast, $\hat{z}_t(l)$, which minimizes the mean square forecast error, is the **conditional expectation** of the future value given all known information.

$$\hat{z}_t(l) = E[z_{t+l} | z_t, z_{t-1}, ...]$$

### 2. The Forecast Equation for an ARMA(p,q) Model

Any ARMA(p,q) model can be written in its random shock form (infinite MA representation):
$$z_t = a_t + \psi_1 a_{t-1} + \psi_2 a_{t-2} + \psi_3 a_{t-3} + ...$$
where $a_t$ is the white noise shock at time $t$, and the $\psi$-weights are calculated from the AR and MA parameters.

A future value $z_{t+l}$ is therefore:
$$z_{t+l} = (a_{t+l} + \psi_1 a_{t+l-1} + ... + \psi_{l-1} a_{t+1}) + (\psi_l a_t + \psi_{l+1} a_{t-1} + ...)$$

The first bracket contains future shocks (unknown), and the second contains past and present shocks (known, as they can be calculated from observed data). The forecast is the expectation of this, which simply sets the expectation of all *future* shocks to zero ($E[a_{t+j}] = 0$ for $j>0$). Thus, the $l$-step ahead forecast is:
$$\hat{z}_t(l) = \psi_l a_t + \psi_{l+1} a_{t-1} + \psi_{l+2} a_{t-2} + ...$$

### 3. Calculating Forecast Probability Limits

The **forecast error**, $e_t(l) = z_{t+l} - \hat{z}_t(l)$, is the part we could not predict:
$$e_t(l) = a_{t+l} + \psi_1 a_{t+l-1} + ... + \psi_{l-1} a_{t+1}$$

The variance of this forecast error is crucial, as it measures the uncertainty in our prediction. Since the $a_t$'s are uncorrelated with variance $\sigma_a^2$:
$$\text{Var}[e_t(l)] = \sigma_a^2 (1 + \psi_1^2 + \psi_2^2 + ... + \psi_{l-1}^2)$$

Assuming the shocks ($a_t$) are normally distributed, the forecast error is also normally distributed. Therefore, a **100(1-α)% probability limit** for the forecast is given by:
$$\hat{z}_t(l) \pm u_{\alpha/2} \cdot \sigma_a \sqrt{1 + \psi_1^2 + \psi_2^2 + ... + \psi_{l-1}^2}$$
where $u_{\alpha/2}$ is the standard normal deviate (e.g., 1.96 for a 95% limit).

---

### Example: Forecasting with an AR(1) Model

Consider the model: $z_t = \phi z_{t-1} + a_t$, where $|\phi|<1$.

*   **$\psi$-weights:** For an AR(1) model, $\psi_j = \phi^j$.
*   **Forecast Equation:** $\hat{z}_t(l) = \phi^l z_t$ (This shows how the forecast decays exponentially to the mean, which is zero here).
*   **Forecast Error Variance:**
    $\text{Var}[e_t(l)] = \sigma_a^2 (1 + \phi^2 + \phi^4 + ... + \phi^{2(l-1)})$
    This is a geometric series, simplifying to $\sigma_a^2 \frac{1 - \phi^{2l}}{1 - \phi^2}$.
*   **95% Probability Limit:**
    $\hat{z}_t(l) \pm 1.96 \cdot \sigma_a \sqrt{\frac{1 - \phi^{2l}}{1 - \phi^2}}$

**Numerical Example:** Let $\phi = 0.8$, $\sigma_a^2 = 1.0$, $z_t = 2.5$, and we want a 2-step ahead forecast ($l=2$).

1.  **Point Forecast:** $\hat{z}_t(2) = (0.8)^2 \cdot 2.5 = 0.64 \cdot 2.5 = 1.6$
2.  **Forecast Error Variance:** $\text{Var}[e_t(2)] = 1 \cdot (1 + (0.8)^2) = 1 + 0.64 = 1.64$
3.  **Standard Error:** $\sqrt{1.64} \approx 1.28$
4.  **95% Probability Limits:** $1.6 \pm (1.96 \cdot 1.28) = 1.6 \pm 2.51$
    → **Lower Limit:** -0.91
    → **Upper Limit:** 4.11

We are 95% confident that the true value $z_{t+2}$ will lie between -0.91 and 4.11.

---

## Key Points & Summary

*   **Forecast Definition:** The optimal $l$-step ahead forecast $\hat{z}_t(l)$ is the conditional expectation of the future value given all present and past information.
*   **Forecast Equation:** It is derived from the random shock form of the model and is a function of the $\psi$-weights and past shocks.
*   **Uncertainty Quantification:** The forecast error variance, built from the $\psi$-weights, is essential for quantifying the accuracy of the forecast.
*   **Probability Limits:** These intervals provide a probabilistic range (e.g., 95% confidence) for where the future observation is expected to lie. They fan out as the lead time $l$ increases, reflecting growing uncertainty the further we forecast into the future.
*   **Assumption:** The calculation of probability limits assumes the white noise process $(a_t)$ is normally distributed. This is a critical assumption to check in practice.

Understanding how to calculate both the forecast and its probability limits is fundamental to making informed, reliable predictions and properly communicating their associated uncertainty.