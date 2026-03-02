Of course. Here is a comprehensive educational note on the topic "Likelihood Function Based on the State-Space Model" for  engineering students.

# Likelihood Function Based on the State-Space Model

## 1. Introduction

In the previous modules, you learned about state-space models (SSMs), which provide a powerful framework for representing dynamic systems. An SSM consists of two equations:
*   **State Equation:** `x_t = F * x_{t-1} + w_t` (describes the evolution of the hidden states)
*   **Measurement Equation:** `y_t = H * x_t + v_t` (describes how observations are generated from the states)

Here, `w_t` and `v_t` are process and measurement noise, typically assumed to be Gaussian with zero mean and covariances `Q` and `R`, respectively.

A critical task in time series analysis is **parameter estimation**—determining the unknown matrices `F`, `H`, `Q`, and `R` from the observed data `Y_T = {y_1, y_2, ..., y_T}`. The most powerful and widely used method for this is **Maximum Likelihood Estimation (MLE)**, which requires the formulation of the **likelihood function**. This module explains how to construct this likelihood function based on the state-space model.

## 2. Core Concepts

### What is the Likelihood Function?

The likelihood function `L(θ | Y_T)` measures the probability of observing the given data `Y_T` for a specific set of model parameters, collectively denoted as `θ` (which includes `F`, `H`, `Q`, `R`). MLE finds the parameter values `θ̂` that maximize this function, i.e., the values that make the observed data most probable.

### The Challenge with SSMs

In a simple statistical model, observations are often independent, making the joint likelihood a simple product of probabilities. In SSMs, the observations `y_t` are **not independent**; they are linked through the latent state `x_t`. This interdependence makes the direct formulation of the likelihood complex.

### The Prediction Error Decomposition

The key to building the likelihood for an SSM is the **prediction error decomposition**. This powerful concept breaks down the joint density of all observations into a product of simpler, conditional densities.

The joint probability density of all observations can be written as:
`p(Y_T; θ) = p(y_1; θ) * p(y_2|y_1; θ) * p(y_3|y_2, y_1; θ) * ... * p(y_T|Y_{T-1}; θ)`

This states that the likelihood of the entire dataset is the product of the likelihood of the first observation and the likelihood of each subsequent observation given all its predecessors.

### The Kalman Filter's Role

The Kalman Filter (KF) is an algorithm that provides the exact solution for the state estimation problem in linear Gaussian SSMs. Crucially for our purpose, as a by-product of its recursive steps, the KF also provides the quantities needed to compute each term in the prediction error decomposition:

1.  **Prediction:** At each step `t`, the KF provides the **one-step-ahead forecast** of the observation:
    `ŷ_{t|t-1} = E[y_t | Y_{t-1}]`

2.  **Innovation (Prediction Error):** The difference between the actual observation and its forecast is called the innovation:
    `ν_t = y_t - ŷ_{t|t-1}`

3.  **Innovation Covariance:** The KF also calculates the covariance matrix of this prediction error:
    `S_t = Cov(ν_t) = H * P_{t|t-1} * H' + R`
    where `P_{t|t-1}` is the predicted state estimation error covariance from the KF.

Under the Gaussian assumption, the forecast error `ν_t` is conditionally normally distributed with mean `0` and covariance `S_t`. Therefore, the conditional density `p(y_t | Y_{t-1}; θ)` is a Gaussian density.

### Formulating the Log-Likelihood Function

It's mathematically convenient to work with the **log-likelihood function**, as products become sums. The log-likelihood for the entire series is:

`log L(θ; Y_T) = Σ_{t=1}^T log p(y_t | Y_{t-1}; θ)`

Since each conditional distribution is Gaussian, we can plug in the formula for the multivariate normal distribution. Ignoring a constant term, the log-likelihood is given by:

`log L(θ; Y_T) = -1/2 Σ_{t=1}^T [ log |S_t| + ν_t' * S_t^{-1} * ν_t ]`

Where:
*   `|S_t|` is the determinant of the innovation covariance matrix at time `t`.
*   `ν_t' * S_t^{-1} * ν_t` is the Mahalanobis distance of the innovation (a scalar).

**In practice:** To evaluate the likelihood for a given parameter set `θ`, you run the Kalman Filter over the entire dataset `Y_T`. At each step `t`, you compute and store the innovation `ν_t` and its covariance `S_t`. The sum of the terms in the equation above gives you the log-likelihood value for that specific `θ`. An optimization algorithm (e.g., Newton-Raphson, BFGS) is then used to find the `θ` that minimizes `-log L(θ; Y_T)` (i.e., maximizes the likelihood).

## 3. Example Scenario

Imagine estimating the parameters of a simple system tracking an object's position and velocity (a standard constant velocity model).

*   **State `x_t`:** `[position; velocity]`
*   **Parameters `θ`:** Perhaps the process noise variance `q` (affecting how erratic the velocity is) and measurement noise variance `r`.
*   **Process:** You propose values for `q` and `r`.
*   **Kalman Filter:** You run the KF with these values. The filter will produce a stream of prediction errors (`ν_t`) and their variances (`S_t`).
*   **Calculate Log-Likelihood:** You compute the sum `-1/2 Σ [ log(S_t) + (ν_t² / S_t) ]` for all time points.
*   **Optimization:** An optimizer adjusts `q` and `r` and repeats the process until it finds the values that result in the highest possible log-likelihood (smallest negative value). These are the Maximum Likelihood Estimates.

## 4. Key Points & Summary

*   **Objective:** The primary goal is to estimate the parameters `θ` of a state-space model from observed data `Y_T`.
*   **Method:** Maximum Likelihood Estimation (MLE) is the preferred method, which requires computation of the likelihood function `L(θ | Y_T)`.
*   **Solution:** For linear Gaussian state-space models, the likelihood function can be efficiently computed **recursively** using the **Kalman Filter**.
*   **Key Concept:** The **Prediction Error Decomposition** allows the joint likelihood to be expressed as a product of conditional likelihoods of the innovations (one-step-ahead forecast errors).
*   **The Formula:** The log-likelihood is `log L(θ; Y_T) = -1/2 Σ_{t=1}^T [ log |S_t| + ν_t' * S_t^{-1} * ν_t ]`, where `ν_t` and `S_t` are direct outputs of the Kalman Filter.
*   **Process:** An optimization algorithm iteratively proposes `θ`, runs the KF to get the log-likelihood, and converges to the value `θ̂` that maximizes it. This makes the observed data `Y_T` the most probable.