# **Probability Mass and Density Functions**

### Definitions and Notations

- **Probability Mass Function (PMF)**: P(X=x) defines the probability of a discrete random variable X taking on the value x.
- **Probability Density Function (PDF)**: f(x) defines the probability of a continuous random variable X taking on a value in the interval [x, x+dx].
- **Random Variable**: X, a variable that can take on different values with different probabilities.

### Key Concepts

- **Probability laws**:
  - **Law of Total Probability**: P(X=x) = ∑ P(X=x|X∈A)P(X∈A)
  - **Bayes' Theorem**: P(A|X=x) = P(X=x|A)P(A) / P(X=x)
- **Properties of PMFs and PDFs**:
  - **Normalization**: ∑ P(X=x) = 1 for PMFs, ∫ f(x) dx = 1 for PDFs
  - **Non-negativity**: P(X=x) ≥ 0 for PMFs, f(x) ≥ 0 for PDFs
  - **Countable additivity**: ∑ P(X=x) = P(X∈S) for finite S
- **Other important formulas**:
  - **Chebyshev inequality**: E[(X-μ)^2] ≥ (σ^2) / 2
  - **Markov inequality**: P(X ≥ a) ≤ E[X] / a

### Important Formulas

- **Probability mass function**: P(X=x) = P(X=x|X∈S) / P(X∈S)
- **Probability density function**: f(x) = P(X=x|X∈[x, x+dx])
- **Cumulative distribution function**: F(x) = P(X≤x) = ∑ P(X=x) for discrete, ∫ f(x) dx for continuous

### Theorems

- **Entropy**: H(X) = - ∑ P(X=x) log2 P(X=x) for discrete, ∫ f(x) log2 f(x) dx for continuous
- **Chain rule for differentiation**: If X = g(U), Y = h(X), then ∂(f ∘ h ∘ g)(u) / ∂u = ∂f(∂h(∂g(u))) / ∂u
