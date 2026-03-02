# Poisson And Normal Distributions - Summary

## Key Definitions

- **Poisson Distribution**: A discrete probability distribution expressing the probability of a given number of events occurring in a fixed interval when events occur with a known constant mean rate λ.

- **Normal (Gaussian) Distribution**: A continuous probability distribution characterized by a symmetric bell-shaped curve, defined by mean μ and variance σ².

- **Standard Normal Distribution**: A normal distribution with mean 0 and variance 1, denoted as N(0,1).

- **Probability Mass Function (PMF)**: Function giving the probability that a discrete random variable equals some value.

- **Probability Density Function (PDF)**: Function describing the probability distribution of a continuous random variable.

## Important Formulas

- **Poisson PMF**: P(X = k) = (λ^k × e^(-λ)) / k!

- **Poisson Mean and Variance**: E(X) = Var(X) = λ

- **Normal PDF**: f(x) = (1 / (σ√(2π))) × e^(-(x-μ)²/(2σ²))

- **Z-score Transformation**: z = (x - μ) / σ

- **Poisson to Normal Approximation**: X ~ Poisson(λ) ≈ N(λ, λ) when λ > 20

## Key Points

1. The Poisson distribution models discrete events occurring independently in a fixed interval with constant average rate λ.

2. The Normal distribution is continuous, symmetric, and fully characterized by its mean μ and standard deviation σ.

3. For Poisson distribution, the mean equals the variance (both equal to λ).

4. The empirical rule states that 68%, 95%, and 99.7% of data fall within 1, 2, and 3 standard deviations of the mean respectively.

5. The standard normal distribution simplifies probability calculations through z-score transformation.

6. Poisson distribution is applicable for modeling website hits, software defects, queue lengths, and network packets.

7. Normal distribution appears in error analysis, measurement noise, and forms the basis for many statistical tests.

8. The Central Limit Theorem ensures that sums of independent random variables approach normal distribution.

## Common Mistakes

1. Confusing discrete Poisson with continuous Normal distributions and using wrong formulas.

2. Forgetting to apply continuity correction when using normal approximation to Poisson.

3. Using wrong values for mean and variance when transforming normal variables.

4. Attempting normal approximation for small λ values where the approximation is inaccurate.

5. Confusing the parameter λ in Poisson (rate and mean) with parameters in other distributions.