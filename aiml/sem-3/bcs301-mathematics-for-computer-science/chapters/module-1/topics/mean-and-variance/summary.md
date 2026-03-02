# Mean and Variance

### Definitions

- **Mean (Expected Value)**: The average value of a random variable, calculated as:
  - `E(X) = ∑xP(x)`
  - `E(X) = μ`
- **Variance**: A measure of the spread or dispersion of a random variable, calculated as:
  - `Var(X) = E((X - μ)^2)`
  - `Var(X) = σ^2`

### Important Formulas

- **Mean of a Constant**: `E(c) = c` for any constant `c`
- **Linearity of Expectation**: `E(aX + b) = aE(X) + b`
- **Variance of a Constant**: `Var(c) = 0` for any constant `c`
- **Variance of a Sum**: `Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)`
- **Standard Deviation**: `σ = √Var(X)`

### Important Theorems

- **Chebyshev's Inequality**: `P(|X - μ| ≥ kσ) ≤ 1/k^2` for any `k > 0`
- **Markov's Inequality**: `P(X ≥ a) ≤ Var(X)/a^2` for any `a > 0`

### Key Properties

- **Symmetry**: `Var(X) = Var(X^(-1))`
- **Zero Mean**: `Var(X) ≠ 0` if and only if `X` is not a constant

### Important Concepts

- **Moment Generation Function**: A function that generates the moments of a random variable
- **Moment-Generating Function**: A function that generates the moments of a random variable using a power series expansion

## Revision Notes

- Review the definitions of mean and variance
- Practice calculating mean and variance for different distributions
- Familiarize yourself with the formulas and theorems listed above
- Review the key properties and concepts related to mean and variance
