# Joint Probability Distribution for Two Discrete Random Variables

### Definitions

- A joint probability distribution for two discrete random variables X and Y is a function that assigns a probability to each possible pair of values, (x, y), where x is in the sample space of X and y is in the sample space of Y.
- The joint probability distribution is denoted by P(X, Y) or P(X, Y; θ) where θ represents the parameter(s) of the distribution.

### Important Formulas

- **Probability Mass Function (PMF) of Joint Distribution**: P(X = x, Y = y) = P(X = x, Y = y; θ)
- **Marginal Probability Mass Functions**: P(X = x) = ∑[P(X = x, Y = y)] over all possible values of Y
  P(Y = y) = ∑[P(X = x, Y = y)] over all possible values of X
- **Conditional Probability Formula**: P(X = x | Y = y) = P(X = x, Y = y) / P(Y = y)
- **Joint Probability Formula**: P(X = x, Y = y) = P(X = x; θ) × P(Y = y; θ)

### Key Theorems

- **Theorem of Total Probability**: P(X = x, Y = y) = ∑[P(X = x, Y = y; θ) × P(θ)]

### Important Theorems

- **Bayes' Theorem**: P(X = x | Y = y) = P(Y = y | X = x) × P(X = x) / P(Y = y)
- **Kolmogorov's 0-1 Law**: If a sequence of independent events has a limit point, then the probability of that limit point is 1.

### Notations

- P(X, Y) is the joint probability distribution of X and Y.
- P(X = x, Y = y) is the joint probability of X = x and Y = y.
- P(X = x) and P(Y = y) are the marginal probability mass functions of X and Y, respectively.
