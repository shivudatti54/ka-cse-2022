# Machine Learning II - Module 4: Markov Chain Monte Carlo (MCMC)

## Introduction

In the realm of machine learning and Bayesian statistics, we often encounter complex, high-dimensional probability distributions. Calculating expectations, marginal probabilities, or other integrals with these distributions is frequently analytically intractable. **Markov Chain Monte Carlo (MCMC)** is a powerful class of algorithms designed to tackle this exact problem. It allows us to generate samples from a target probability distribution, even when its normalization constant (the notoriously difficult-to-compute partition function) is unknown. By drawing these samples, we can approximate complex integrals through simple averages, making the impossible possible.

## Core Concepts

### 1. The Monte Carlo Principle

The foundation of MCMC is built on two ideas:

*   **Monte Carlo:** This is a general statistical technique that uses random sampling to approximate numerical results. The core idea is that if we want to estimate the expectation of a function $f(x)$ under a distribution $P(x)$ (e.g., $\mathbb{E}[f]$), we can draw independent and identically distributed (i.i.d.) samples $\{x^{(1)}, x^{(2)}, ..., x^{(S)}\}$ from $P(x)$ and compute:
    $$\mathbb{E}[f] \approx \frac{1}{S} \sum_{s=1}^{S} f(x^{(s)})$$
    This approximation becomes exact as the number of samples $S$ goes to infinity.

*   **The Problem:** For complex distributions, especially in high dimensions, we cannot sample from $P(x)$ directly. This is where the second part, the Markov Chain, comes in.

### 2. Markov Chains

A Markov chain is a stochastic process where the next state depends *only* on the current state, not on the entire history (the Markov Property). It's defined by a **transition probability** $T(x^{(s+1)} | x^{(s)})$, which specifies the probability of moving from state $x^{(s)}$ to state $x^{(s+1)}$.

Under certain conditions (ergodicity), a Markov chain will converge to a unique **stationary distribution** $\pi(x)$. This means that after a sufficient number of steps (the "burn-in" period), the states of the chain will be samples from $\pi(x)$, regardless of the starting state.

### 3. Combining the Two: MCMC

MCMC cleverly combines these concepts. The goal is to design a Markov chain whose stationary distribution $\pi(x)$ is exactly our **target distribution** $P(x)$ from which we want to sample. We run the chain for a long time, discard the initial burn-in samples, and then use the subsequent states as our dependent, but approximately fair, samples from $P(x)$.

### The Metropolis-Hastings Algorithm

The most famous MCMC algorithm is Metropolis-Hastings. It provides a way to create the correct Markov chain without needing to know the full normalization constant of $P(x)$. We only need to know a function $f(x)$ proportional to $P(x)$ (e.g., $P^*(x) = P(x) \cdot Z$, where $Z$ is the unknown constant).

**Steps of the Algorithm:**
1.  **Initialize:** Start with an initial state $x^{(0)}$.
2.  **Propose:** For each iteration $s$, propose a new state $x'$ by sampling from a simpler **proposal distribution** $Q(x' | x^{(s)})$ (e.g., a Gaussian centered on $x^{(s)}$).
3.  **Accept/Reject:** Calculate the acceptance probability:
    $$A(x', x^{(s)}) = \min \left(1, \frac{P^*(x') \cdot Q(x^{(s)} | x')}{P^*(x^{(s)}) \cdot Q(x' | x^{(s)})} \right)$$
    This ratio ensures detailed balance, guaranteeing the correct stationary distribution.
4.  **Sample:** Draw a random number $u$ from $\text{Uniform}(0,1)$.
    *   If $u \leq A$, **accept** the move: $x^{(s+1)} = x'$.
    *   Else, **reject** the move: $x^{(s+1)} = x^{(s)}$.
5.  **Repeat:** Iterate steps 2-4 for a large number of steps.

**Example:** Imagine we want to sample from a complex 1D posterior distribution $P(\theta | data)$. We initialize $\theta_0$. Our proposal $Q$ could be $N(\theta^{(s)}, 1)$. We calculate $P^*$ using Bayes' Theorem (likelihood × prior, ignoring the marginal likelihood $Z$). The acceptance ratio simplifies to:
$$A = \min \left(1, \frac{P^*(\theta')}{P^*(\theta^{(s)})} \right)$$
if $Q$ is symmetric. If the proposed $\theta'$ is in a region of higher probability, we always accept it. If it's in a lower probability region, we might still accept it with a probability proportional to the ratio.

## Gibbs Sampling

Gibbs Sampling is a special case of Metropolis-Hastings where the acceptance probability is always 1. It's highly useful when we can sample from the conditional distribution of each variable given all the others.

For a random vector $x = (x_1, x_2, ..., x_D)$:
1.  Initialize $x^{(0)} = (x_1^{(0)}, x_2^{(0)}, ..., x_D^{(0)})$.
2.  For each iteration $s$:
    *   Sample $x_1^{(s+1)} \sim P(x_1 | x_2^{(s)}, x_3^{(s)}, ..., x_D^{(s)})$
    *   Sample $x_2^{(s+1)} \sim P(x_2 | x_1^{(s+1)}, x_3^{(s)}, ..., x_D^{(s)})$
    *   ...
    *   Sample $x_D^{(s+1)} \sim P(x_D | x_1^{(s+1)}, x_2^{(s+1)}, ..., x_{D-1}^{(s+1)})$
3.  The new state $x^{(s+1)}$ is the collection of all these samples.

This cycle creates a Markov chain that converges to the joint target distribution $P(x)$.

## Key Points & Summary

| **Aspect** | **Description** |
| :--- | :--- |
| **Purpose** | To generate samples from a complex target distribution $P(x)$ when direct sampling is impossible and the normalization constant is unknown. |
| **How it Works** | Constructs a Markov Chain whose stationary distribution is the target $P(x)$. After a burn-in period, the chain's states are used as dependent samples. |
| **Key Idea** | Uses a proposal/acceptance mechanism (Metropolis-Hastings) or conditional sampling (Gibbs) to explore the state space. |
| **Requirement** | Only requires a function $f(x)$ *proportional* to the target density $P(x)$; the exact normalization is not needed. |
| **Output** | Produces a sequence of **correlated samples**. This correlation must be considered when estimating variances (often requiring more samples than i.i.d. sampling). |
| **Applications** | Bayesian inference (posterior sampling), training Boltzmann machines, statistical physics, and optimization. |
| **Burn-in** | Initial samples must be discarded as the chain has not yet converged to the stationary distribution. |
| **Challenges** | Choosing a good proposal distribution $Q$, determining convergence (burn-in), and dealing with the high autocorrelation between samples. |