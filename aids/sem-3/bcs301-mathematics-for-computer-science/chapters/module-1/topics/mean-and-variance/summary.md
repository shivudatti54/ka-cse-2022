# Mean and Variance

### Definitions

- **Mean (Expected Value)**:
  - Definition: The long-run average of a random variable X, denoted as E(X) or μ (mu)
  - Formula: μ = ∑xP(x) or μ = E(X) = ∫xf(x)dx (for continuous distributions)
- **Variance**:
  - Definition: The average of the squared differences from the mean, denoted as Var(X) or σ^2 (sigma squared)
  - Formula: σ^2 = E[(X - μ)^2]

### Important Formulas

- **Mean and Variance of a Discrete Random Variable**:
  - μ = ∑xP(x)x
  - σ^2 = ∑(x - μ)^2P(x)
- **Mean and Variance of a Continuous Random Variable**:
  - μ = ∫xf(x)dx
  - σ^2 = ∫(x - μ)^2f(x)dx

### Theorems

- **Linearity of Expectation**:
  - E[aX + b] = aE(X) + b, where a and b are constants
- **Independence of Random Variables**:
  - If X and Y are independent, then Cov(X, Y) = 0
- **Cauchy-Schwarz Inequality**:
  - |Cov(X, Y)| ≤ √(Var(X)Var(Y))

### Important Results

- **Chebyshev's Inequality**:
  - P(|X - μ| ≥ kσ) ≤ 1/k^2, where k is a positive constant
- **Central Limit Theorem (CLT)**:
  - The distribution of the mean of a large sample of independent and identically distributed random variables converges to a normal distribution, regardless of the original distribution of the variables.
