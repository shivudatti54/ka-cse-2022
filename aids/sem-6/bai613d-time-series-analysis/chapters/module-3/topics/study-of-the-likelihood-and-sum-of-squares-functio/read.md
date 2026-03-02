Of course. Here is a comprehensive educational note on the topic for  engineering students.

# Module 3: Study of the Likelihood and Sum-of-Squares Functions

## 1. Introduction

In Time Series Analysis, after identifying a suitable ARIMA model (e.g., AR(1), MA(1), ARMA(1,1)), we must **estimate its parameters** (like ϕ, θ, and μ). The values we choose for these parameters critically impact the model's accuracy and predictive power. This module focuses on two fundamental principles used for this estimation: the **Sum-of-Squares Function** (S(·)) and the **Likelihood Function** (L(·)). Both provide a measure of how well a model, with a given set of parameters, fits the observed data.

## 2. Core Concepts

### 2.1. The Sum-of-Squares Function (S(𝛽))

The Sum-of-Squares function is intuitively connected to the concept of model errors. For a time series model, the error at time `t`, `a_t`, is the difference between the observed value `z_t` and the model's prediction `ẑ_t`.

*   **Idea:** Find the parameter values (e.g., ϕ for an AR(1) model) that minimize the total squared error. A smaller sum-of-squares indicates a better fit.
*   **Definition:** For a parameter vector **𝛽** (e.g., **𝛽** = [ϕ₁, ϕ₂,..., θ₁, θ₂,...]), the function is defined as:
    $$S(\boldsymbol{\beta}) = \sum_{t=1}^{n} a_t^2(\boldsymbol{\beta})$$
    where `a_t(𝛽)` are the residuals calculated based on the parameters **𝛽**.
*   **Use:** The parameter estimates **𝛽̂** are found by minimizing `S(𝛽)`.
    $$\hat{\boldsymbol{\beta}} = \arg \min_{\boldsymbol{\beta}} S(\boldsymbol{\beta})$$
    This is often achieved using numerical optimization algorithms like the Newton-Raphson method.

### 2.2. The Likelihood Function (L(𝛽))

The Likelihood Function takes a more probabilistic approach. It answers the question: "**Given a specific set of parameters 𝛽, what is the probability (or likelihood) of observing the data we actually have?**"

*   **Assumption:** The errors (`a_t`) are typically assumed to be independently and identically distributed (i.i.d.) normal random variables, i.e., `a_t ~ N(0, σ_a²)`.
*   **Definition:** The likelihood `L` is the joint probability density function of all observations, viewed as a function of the parameters **𝛽** and `σ_a²`.
    $$L(\boldsymbol{\beta}, \sigma_a^2 | \mathbf{z}) = p(z_1, z_2, ..., z_n | \boldsymbol{\beta}, \sigma_a^2)$$
*   **Maximum Likelihood Estimation (MLE):** We seek the parameter values **𝛽̂** and `σ̂_a²` that **maximize** this likelihood function. These values make the observed data "most probable."
*   **The Log-Likelihood:** Because the likelihood involves a product of many small probabilities, it's standard to work with the **log-likelihood** `l(·) = log L(·)`, which converts the product into a sum and is easier to maximize.
    $$l(\boldsymbol{\beta}, \sigma_a^2) = -\frac{n}{2} \log(2\pi) - \frac{n}{2} \log(\sigma_a^2) - \frac{S(\boldsymbol{\beta})}{2\sigma_a^2} + \text{(a term involving initial values)}$$
    The term `S(𝛽)` is the same sum-of-squares function defined earlier.

### 2.3. The Connection Between S(𝛽) and L(𝛽)

The log-likelihood function reveals a crucial link:
$$l(\boldsymbol{\beta}, \sigma_a^2) = \text{constant} - \frac{n}{2} \log(\sigma_a^2) - \frac{S(\boldsymbol{\beta})}{2\sigma_a^2}$$

From this, we can derive two important results:
1.  For a fixed **𝛽**, the value of `σ_a²` that maximizes `l(·)` is `σ̂_a² = S(𝛽)/n`.
2.  Substituting this back into the log-likelihood, maximizing `l(·)` is largely equivalent to minimizing `S(𝛽)`.

Therefore, **under the assumption of normally distributed errors, the Maximum Likelihood Estimators (MLE) and the Least-Squares Estimators (which minimize S(𝛽)) are nearly identical**, especially for large sample sizes (`n`).

## 3. Example: AR(1) Model

Consider a zero-mean AR(1) process: `z_t = ϕ z_{t-1} + a_t`, with `a_t ~ N(0, σ_a²)`.

*   **Sum-of-Squares:** The conditional sum-of-squares (ignoring the initial value `z_0`) is:
    $$S(\phi) = \sum_{t=2}^{n} a_t^2 = \sum_{t=2}^{n} (z_t - \phi z_{t-1})^2$$
    Minimizing this with respect to `ϕ` leads to the familiar least-squares estimator:
    $$\hat{\phi} = \frac{\sum_{t=2}^{n} z_t z_{t-1}}{\sum_{t=2}^{n} z_{t-1}^2}$$

*   **Likelihood:** The exact likelihood function for the AR(1) model is more complex as it must account for the distribution of the initial value `z_0`. However, for large `n`, the conditional MLE (which conditions on `z_0`) is virtually the same as the least-squares estimator above.

## 4. Key Points & Summary

| Aspect | Sum-of-Squares (Least-Squares) | Likelihood (Maximum Likelihood) |
| :--- | :--- | :--- |
| **Philosophy** | Minimize the total squared error between observed and predicted values. | Find the parameters that make the observed data most probable. |
| **Assumption** | Minimal (only that the model form is correct). | Stronger (requires a full probability model, almost always normality of errors). |
| **Calculation** | Often simpler, direct minimization of `S(𝛽)`. | More complex, involves maximizing `L(𝛽)` or `l(𝛽)`. |
| **Result** | Least-Squares Estimates (LSE). | Maximum Likelihood Estimates (MLE). |
| **Relationship** | Under the normal error assumption, MLE ≈ LSE. MLE has a solid theoretical foundation for constructing confidence intervals and hypothesis tests. |

*   **Summary:**
    *   Both `S(𝛽)` and `L(𝛽)` are **objective functions** used to estimate time series model parameters.
    *   The **Sum-of-Squares Function** is the foundation of the **Least-Squares** method.
    *   The **Likelihood Function** is the foundation of the **Maximum Likelihood Estimation** method.
    *   For ARIMA models with **normally distributed innovations**, minimizing the sum-of-squares is **equivalent to maximizing the likelihood** (especially for conditional models).
    *   MLE is a more general and powerful technique with optimal statistical properties (e.g., consistency, efficiency) for large samples, making it the preferred method in most modern software packages.

** Perspective:** Understanding this equivalence is key. You will use software (like R or Python) that employs these principles to automatically find the best parameter estimates for your ARIMA models.