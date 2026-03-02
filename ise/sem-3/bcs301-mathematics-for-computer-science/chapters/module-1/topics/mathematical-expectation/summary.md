# Mathematical Expectation

### Key Points

- **Definition**: The expected value or mathematical expectation of a discrete random variable X is the sum of each possible value of X multiplied by its probability of occurrence.
- **Formula**: E(X) = ∑xP(X=x)
- **Continuous case**: E(X) = ∫xf(x)dx, where f(x) is the probability density function of X

### Important Formulas

- **Linearity of expectation**: E(aX + b) = aE(X) + b for constants a and b
- **Law of iterated expectations**: E(E(X|Y)) = E(X)
- **Conditional expectation**: E(X|Y) = ∑xE\_{X|Y}(x)

### Theorems

- **Expectation is a linear functional**: E(aX + b) = aE(X) + b for constants a and b
- **Expectation is subadditive**: E(X + Y) ≤ E(X) + E(Y)

### Important Concepts

- **Random variable**: A function that assigns a numerical value to each possible outcome of a random experiment
- **Probability distribution**: A function that assigns a probability to each possible value of a random variable
- **Expected value**: A measure of the central tendency of a random variable

### Important Theorems and Results

- **Chebyshev's inequality**: For any random variable X with expected value E(X) and variance Var(X), P(|X - E(X)| ≥ k) ≤ Var(X)/k^2
- **Markov's inequality**: For any non-negative random variable X with expected value E(X), P(X ≥ k) ≤ E(X)/k
