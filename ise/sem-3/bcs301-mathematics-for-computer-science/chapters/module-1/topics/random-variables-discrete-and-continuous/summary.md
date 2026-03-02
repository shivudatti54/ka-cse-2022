# **Random Variables (Discrete and Continuous)**

## **Definitions and Notations**

- A random variable is a function that assigns a numerical value to each outcome of a random experiment.
- Let X be a random variable defined on a probability space (Ω, Σ, P).
- X is said to be a discrete random variable if it takes on a finite or countable number of values, and a continuous random variable if it takes on a countably infinite number of values.

## **Discrete Random Variables**

- **Probability Mass Function (PMF)**: P(X = x) = p(x)
- **Expected Value (E)**: E(X) = ∑xp(x)
- **Variance (Var)**: Var(X) = E(X^2) - (E(X))^2
- **Standard Deviation (σ)**: σ = √Var(X)

## **Continuous Random Variables**

- **Probability Density Function (PDF)**: f(x) = P(a ≤ X ≤ b)
- **Cumulative Distribution Function (CDF)**: F(x) = P(X ≤ x)
- **Expected Value (E)**: E(X) = ∫xf(x)dx
- **Variance (Var)**: Var(X) = E(X^2) - (E(X))^2
- **Standard Deviation (σ)**: σ = √Var(X)

## **Important Theorems and Results**

- **Law of Large Numbers (LLN)**: As n → ∞, (1/n)∑X_i → E(X)
- **Central Limit Theorem (CLT)**: As n → ∞, (1/√n)∑(X_i - E(X_i)) → N(0, σ^2)
- **Chebyshev's Inequality**: P(|X - E(X)| ≥ kσ) ≤ 1/k^2

## **Key Formulas and Equations**

- Poisson distribution: P(X = k) = (e^(-λ)λ^k)/k!
- Binomial distribution: P(X = k) = (nCk) × p^k × (1-p)^(n-k)
- Normal distribution: f(x) = (1/√(2πσ^2)) × e^(-(x-μ)^2/(2σ^2))
