Of course. Here is a comprehensive educational note on the requested topic, formatted for  engineering students.

# Module 3: Study of the Likelihood and Sum-of-Squares Functions

## 1. Introduction

In Time Series Analysis, after identifying a potential model (like AR, MA, or ARMA), we need to **estimate its parameters** (e.g., the ϕ's in an AR model or the θ's in an MA model). This module focuses on the two most powerful and fundamental methods for this estimation: the **Method of Maximum Likelihood** and the closely related **Method of Least Squares (Sum-of-Squares)**. These methods provide the "best-fitting" parameters based on the observed data.

## 2. Core Concepts

### 2.1 The Principle of Maximum Likelihood

The Maximum Likelihood Estimation (MLE) method chooses the parameter values that make the **observed data most probable**.

*   **The Likelihood Function (`L`)**: For a time series model with parameters **β** (e.g., β = [ϕ₁, ϕ₂, θ₁, σₐ²]) and observed data **z₁, z₂, ..., zₙ**, the likelihood function `L(β | z)` is the joint probability density function of the observations, viewed as a function of the parameters β.
*   **The Goal**: Find the parameter values **β̂** that maximize `L(β | z)`. We call **β̂** the Maximum Likelihood Estimators.
*   **The Log-Likelihood (`l`)**: Because the likelihood `L` is often a product of many terms (and thus difficult to maximize), we almost always work with the natural logarithm of the likelihood, the **log-likelihood function `l = ln(L)`**. Since the logarithm is a monotonically increasing function, maximizing `l` is equivalent to maximizing `L`. This transforms the product into a sum, which is much easier to differentiate and optimize.

    `l(β) = ln[L(β | z)]`

*   **Maximization**: We find the estimates by taking the partial derivatives of `l(β)` with respect to each parameter in β, setting them to zero, and solving the resulting system of equations (known as the **likelihood equations**). This often requires numerical optimization techniques.

### 2.2 The Sum-of-Squares Function (`S(β)`)

For the special case where the random shocks (innovations) `aₜ` are **Gaussian (normally distributed)**, the method of Maximum Likelihood is directly related to the Method of Least Squares.

*   **The Concept**: The sum-of-squares function `S(β)` is the sum of the squared residuals (the estimated `aₜ` values) from the model.
    `S(β) = Σ(aₜ̂)² = Σ (zₜ - zₜ̂)²`
    where `zₜ̂` is the model's forecast or conditional expectation of `zₜ` given the past values and the model parameters.

*   **The Link to MLE**: Under the assumption of normally distributed white noise (`aₜ ~ N(0, σₐ²)`), the log-likelihood function can be shown to be:
    `l(β) = - (n/2)ln(2π) - (n/2)ln(σₐ²) - (1/(2σₐ²)) * S(β)`

    From this equation, it's clear that for a fixed value of `σₐ²`, **maximizing the log-likelihood `l(β)` is equivalent to minimizing the sum-of-squares function `S(β)`**. This establishes the Least Squares method as a form of Maximum Likelihood estimation under the normality assumption.

### 2.3 Conditional vs. Unconditional Likelihood

In practice, calculating the exact likelihood can be complex because the start-up values for the time series (e.g., `z₀`, `z₋₁`, `a₀`) are unknown. Two common approximations are used:

1.  **Conditional Likelihood**: We condition on the first few observations and assume the unknown pre-sample values of `aₜ` are zero. For an ARMA(p,q) model, we condition on the first `p` observations (`z₁,..., zₚ`) and set `a₀ = a₋₁ = ... = a₋q+1 = 0`. This simplifies the calculation, and the resulting function `S(β)` is called the **conditional sum-of-squares**. It works well for long time series.
2.  **Unconditional (Exact) Likelihood**: This method uses the full joint probability distribution of the data, accounting for the start-up values using the backcasting technique or the state-space model Kalman filter. It is more computationally intensive but is preferred for shorter series.

## 3. Example: AR(1) Model

Consider an AR(1) model: `zₜ = ϕ zₜ₋₁ + aₜ`, where `aₜ ~ N(0, σₐ²)`.

*   **Conditional Approach**: We condition on the first observation `z₁`. The conditional sum-of-squares function is:
    `S(ϕ) = Σ (aₜ)² = Σ (zₜ - ϕ zₜ₋₁)²` for `t=2 to n`.

*   **Minimization**: To find the Least Squares estimate `ϕ̂`, we minimize `S(ϕ)` with respect to ϕ.
    `dS(ϕ)/dϕ = -2 Σ zₜ₋₁ (zₜ - ϕ zₜ₋₁) = 0`
    Solving this gives the familiar estimator: `ϕ̂ = (Σ zₜ zₜ₋₁) / (Σ zₜ₋₁²)` for `t=2 to n`.

This `ϕ̂` is the Conditional Least Squares estimator and, under normality, the Conditional Maximum Likelihood estimator.

## 4. Key Points & Summary

| Key Point | Explanation |
| :--- | :--- |
| **Primary Goal** | To estimate the parameters of a time series model (AR, MA, ARMA) from observed data. |
| **Maximum Likelihood (ML)** | Finds the parameter values that make the observed data the most probable. It is a very general and powerful statistical method. |
| **Sum-of-Squares (Least Squares)** | Minimizes the sum of squared forecast errors. Under the assumption of **normality**, it is equivalent to ML. |
| **Log-Likelihood (`l`)** | The natural log of the likelihood function. It is used for practical computation instead of the raw likelihood `L`. |
| **Conditional vs. Unconditional** | The **conditional** approach simplifies calculation by assuming initial values are known/zero. The **unconditional** approach is exact but more complex. |
| **Requires Numerical Methods** | For models more complex than AR(1) or MA(1), closed-form solutions are rare. Parameters are estimated using numerical optimization algorithms (e.g., Newton-Raphson). |
| **Estimates are Asymptotic** | The properties of ML estimators (like unbiasedness, efficiency) are guaranteed primarily for large sample sizes (`n -> ∞`). |

In summary, the study of the likelihood and sum-of-squares functions provides the theoretical and computational foundation for parameter estimation in time series models, forming a critical step in the Box-Jenkins methodology for model building.