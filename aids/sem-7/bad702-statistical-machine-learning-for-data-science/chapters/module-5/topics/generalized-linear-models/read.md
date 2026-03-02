# Module 5: Generalized Linear Models (GLMs)

## Introduction

Generalized Linear Models (GLMs) are a broad and flexible extension of traditional linear regression. While linear regression is powerful, it makes strong assumptions (e.g., normally distributed errors, constant variance) that are often violated by real-world data, such as binary outcomes (pass/fail) or count data (number of events). GLMs overcome these limitations by allowing the response variable to follow any distribution from the **exponential family** (e.g., Gaussian, Binomial, Poisson). This makes them an indispensable tool for a data scientist tackling diverse problems like spam detection, risk modeling, and demand forecasting.

## Core Concepts of GLMs

A GLM generalizes linear regression through three key components:

### 1. Random Component (The Probability Distribution)

This specifies the probability distribution of the response variable `Y`. Unlike linear regression, which assumes a Gaussian (Normal) distribution, GLMs can use any distribution from the exponential family. Common choices include:
*   **Gaussian:** For continuous, real-valued data (standard linear regression).
*   **Binomial:** For binary/binary-classification data (e.g., 0/1, success/failure).
*   **Poisson:** For count data (e.g., number of customers arriving in an hour).

### 2. Systematic Component (The Linear Predictor)

This is the familiar linear combination of the input features and model parameters, just like in linear regression.
`η = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ`
where:
*   `η` is the linear predictor.
*   `β₀` is the intercept.
*   `β₁, ..., βₚ` are the coefficients for features `x₁, ..., xₚ`.

### 3. Link Function, `g(.)`

This is the crucial element that *generalizes* the linear model. The link function `g(.)` connects the **mean of the response variable** `μ = E(Y)` to the **linear predictor** `η`.
`g(μ) = η`
or equivalently,
`μ = g⁻¹(η)`

The link function's job is to map the range of the mean `μ` (which is constrained by the distribution) to the entire real number line (`-∞` to `+∞`), which is the domain of the linear predictor `η`.

## Common GLMs and Their Applications

| Model Type | Response Distribution | Default Link Function | Link Function | Inverse Link (Mean Function) | Typical Application |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Linear Regression** | Gaussian | Identity | `η = g(μ) = μ` | `μ = η` | Predicting house prices |
| **Logistic Regression** | Binomial | Logit | `η = log(μ/(1-μ))` | `μ = 1/(1 + e⁻η)` | Binary classification (spam detection) |
| **Poisson Regression** | Poisson | Log | `η = log(μ)` | `μ = eη` | Modeling count data (website visits) |

### Example: Logistic Regression as a GLM

Let's say you want to predict whether a student will pass (`Y=1`) or fail (`Y=0`) an exam based on their hours of study (`x`).

1.  **Random Component:** The outcome is binary, so we choose the **Binomial** distribution for `Y`.
2.  **Systematic Component:** We define our linear predictor: `η = β₀ + β₁ * (Hours_Studied)`.
3.  **Link Function:** We use the **logit** link function to connect the mean `μ` (which here is the probability of passing, `P(Y=1)`) to `η`.
    `log( P(Y=1) / (1 - P(Y=1)) ) = η = β₀ + β₁ * (Hours_Studied)`

To interpret this, we solve for the probability using the inverse link (the logistic function):
`P(Y=1) = 1 / (1 + e⁻η) = 1 / (1 + e^{-(β₀ + β₁*x)})`

This elegant formulation ensures that no matter what value the linear predictor `η` takes, the output probability will always be squeezed between 0 and 1.

## Parameter Estimation

The parameters `β` of a GLM are typically estimated using **Maximum Likelihood Estimation (MLE)**, not ordinary least squares. The optimization is performed iteratively using algorithms like **Iteratively Reweighted Least Squares (IRLS)**.

## Key Points & Summary

*   **Core Idea:** GLMs extend linear models to handle non-normal response variables.
*   **Three Pillars:** A GLM is defined by its 1) **Random Component** (distribution), 2) **Systematic Component** (linear predictor), and 3) **Link Function**.
*   **Exponential Family:** The response variable `Y` must follow a distribution from the exponential family (Gaussian, Binomial, Poisson, Gamma, etc.).
*   **Link Function:** Connects the mean of the response `μ` to the linear predictor `η`. It transforms the prediction to the appropriate scale.
*   **Flexibility:** By choosing the appropriate distribution and link function, GLMs can model a vast array of data types, making them a foundational tool for regression and classification tasks in statistical machine learning.
*   **Estimation:** Parameters are estimated via Maximum Likelihood, often using iterative numerical methods.