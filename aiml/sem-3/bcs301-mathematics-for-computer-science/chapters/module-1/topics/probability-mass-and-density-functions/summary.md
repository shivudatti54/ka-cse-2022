# Probability Mass and Density Functions

### Definitions

- **Probability Mass Function (PMF)**: A function that describes the probability distribution of a discrete random variable. It assigns a non-negative value to each possible outcome of the variable.
- **Probability Density Function (PDF)**: A function that describes the probability distribution of a continuous random variable. It assigns a non-negative value to each possible outcome of the variable, representing the relative likelihood of each outcome.

### Notations

- **X**: Random variable
- **P(X=x)**: Probability of outcome x
- **P(X) = ∑ P(X=x) for discrete**: Sum of probabilities of all possible outcomes
- **f(x) = P(X=x) for continuous**: Probability density at point x
- **F(x) = ∫[a, x] f(t) dt for continuous**: Cumulative distribution function

### Formulas and Theorems

- **Probability Rule**: P(X ∈ A) = P(X=a1) + P(X=a2) + ... + P(X=an)
- **Normalizing Constant**: ∫[a, ∞) f(x) dx = 1 for PDF, P(X=a) = 1 for PMF
- **Chebyshev's Inequality**: E(X^2) ≥ (E(X))^2
- **Markov's Inequality**: P(X ≥ a) ≤ E(X)/a

### Important Properties

- **Non-Negativity**: f(x) ≥ 0 for PDF, P(X=x) ≥ 0 for PMF
- **Normalization**: ∫[a, ∞) f(x) dx = 1 for PDF, P(X=a) = 1 for PMF
- **Monotonicity**: f(x1) ≤ f(x2) if x1 ≤ x2 for PDF, P(X=x1) ≤ P(X=x2) if x1 ≤ x2 for PMF

### Key Concepts

- **Discrete Distribution**: PMF
- **Continuous Distribution**: PDF
- **Random Variable**: Can take on any value from a sample space
- **Probability Distribution**: A function that assigns probabilities to outcomes in a sample space
