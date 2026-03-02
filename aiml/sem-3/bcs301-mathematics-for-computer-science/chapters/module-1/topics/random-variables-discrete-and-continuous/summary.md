# **Random Variables (Discrete and Continuous)**

## **Definitions and Notations**

- A **random variable** is a function that maps a sample space to the real numbers.
- Discrete random variable: X(X takes on a countable number of values)
- Continuous random variable: X(X takes on a uncountable number of values)

## **Properties of Random Variables**

- **Mean (Expected Value)**:
  - Discrete: E(X) = ∑xP(X=x)
  - Continuous: E(X) = ∫x f(x) dx
- **Variance**:
  - Discrete: Var(X) = E(X^2) - E(X)^2
  - Continuous: Var(X) = ∫(x-E(X))^2 f(x) dx
- **Standard Deviation**: σ = √Var(X)

## **Theorems and Formulas**

- **Law of Large Numbers (LLN)**: As n→∞, (X1 + X2 + ... + Xn)/n → E(X)
- **Central Limit Theorem (CLT)**: As n→∞, (X1 + X2 + ... + Xn)/√n → N(0, σ^2)
- **Probability Mass Function (PMF)**:
  - Discrete: P(X=x) = f(x)
  - Continuous: P(X≤x) = F(x), where F(x) is the CDF
- **Cumulative Distribution Function (CDF)**:
  - Continuous: F(x) = P(X≤x)

## **Key Distributions**

- **Bernoulli Distribution**:
  - P(X=0) = p, P(X=1) = 1-p
- **Binomial Distribution**:
  - P(X=k) = C(n,k) \* p^k \* (1-p)^(n-k)
- **Poisson Distribution**:
  - P(X=k) = (e^(-λ) \* (λ^k)) / k!
- **Normal Distribution**:
  - P(X≤x) = Φ((x-μ)/σ)
  - Φ(x) is the CDF of the standard normal distribution
