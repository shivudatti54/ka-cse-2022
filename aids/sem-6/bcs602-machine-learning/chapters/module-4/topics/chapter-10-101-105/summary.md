# Chapter 10 Revision Notes: Bayesian Learning

### Introduction to Bayesian Learning

- **Definition:** Bayesian learning is a probability-based learning method that updates the probability of a hypothesis based on new data.
- **Key concept:** Bayes' theorem, which describes the update of probabilities using prior and likelihood information.

### Bayes' Theorem

- **Formula:** P(H|D) = P(D|H) \* P(H) / P(D)
- **Definition:** Posterior probability of a hypothesis H given data D
- **Prior probability:** P(H), initial probability of a hypothesis
- **Likelihood:** P(D|H), probability of data given a hypothesis

### Probability Theory Basics

- **Definition:** Probability of an event E: P(E) = (Number of favorable outcomes) / (Total number of outcomes)
- **Theorem:** Law of Total Probability
  - P(E) = ∑ P(E|H_i) \* P(H_i)

### Gaussian Distribution (Normal Distribution)

- **Formula:** f(x) = (1 / √(2πσ^2)) \* exp(-(x - μ)^2 / (2σ^2))
- **Definition:** Probability density function of a normal distribution
- **Mean (μ):** Expected value of the distribution
- **Variance (σ^2):** Spread of the distribution

### Linear Regression (Bayesian)

- **Formula:** P(θ|D) ∝ P(D|θ) \* P(θ)
- **Definition:** Posterior probability of a parameter θ given data D
- **Prior distribution:** P(θ), initial probability of a parameter
- **Likelihood:** P(D|θ), probability of data given a parameter

### Important Formulas and Definitions

| Formula/Definition                                                 | Description                                 |
| ------------------------------------------------------------------ | ------------------------------------------- | ----------------- | ---------------------------- |
| P(H                                                                | D) = P(D                                    | H) \* P(H) / P(D) | Bayes' theorem               |
| P(E) = (Number of favorable outcomes) / (Total number of outcomes) | Probability of an event                     |
| f(x) = (1 / √(2πσ^2)) \* exp(-(x - μ)^2 / (2σ^2))                  | Gaussian distribution (normal distribution) |
| P(θ                                                                | D) ∝ P(D                                    | θ) \* P(θ)        | Linear regression (Bayesian) |
