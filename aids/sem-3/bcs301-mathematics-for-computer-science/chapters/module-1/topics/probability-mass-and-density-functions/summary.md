# Probability Mass and Density Functions

### Definitions and Notations

- **Probability Mass Function (PMF)**: A function that assigns a real number to each possible outcome in a random experiment, representing the probability of that outcome.
- **Probability Density Function (PDF)**: A function that assigns a non-negative real number to each possible outcome in a continuous random experiment, representing the probability density of that outcome.
- **Random Variable**: A variable that can take on different values based on the outcome of a random experiment.

### Key Formulas and Theorems

- **Probability Mass Function (PMF)**:
  - $P(X = x) = p(x)$ for discrete random variables
  - $\sum_{x} p(x) = 1$
- **Probability Density Function (PDF)**:
  - $f(x) = p(x)$ for continuous random variables
  - $\int_{-\infty}^{\infty} f(x) dx = 1$
- **Mean (Expected Value)**:
  - $E(X) = \sum_{x} xP(X = x) = \int_{-\infty}^{\infty} x f(x) dx$
- **Variance**:
  - $\sigma^2 = E(X^2) - E(X)^2 = \sum_{x} (x - E(X))^2 P(X = x)$
- **Central Limit Theorem (CLT)**:
  - The distribution of the mean of a large sample of independent and identically distributed random variables will be approximately normal, regardless of the original distribution.

### Important Concepts

- **Discrete vs. Continuous Random Variables**: Discrete variables take on countable values, while continuous variables can take on any real value.
- **Unimodality and Symmetry**: A probability distribution is unimodal if it has a single peak, and symmetric if it is symmetric about the mean.
- **Moment Generating Function (MGF)**: A function that encodes the moments of a random variable and can be used to derive the distribution of a sum of independent random variables.

### Important Theorems

- **Probability Rule**: $P(A \cap B) = P(A)P(B|A)$
- **Law of Total Probability**: $P(A) = \sum_{B} P(A|B)P(B)$

By reviewing these key points, you'll be well-prepared for your exams on probability mass and density functions.
