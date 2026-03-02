# Random Variables (Discrete and Continuous)

### Definitions

- **Random Variable**: A function that assigns a numerical value to each outcome in a sample space.
- **Discrete Random Variable**: A random variable that can take on only a countable number of distinct values.
- **Continuous Random Variable**: A random variable that can take on any value within a given interval.

### Key Concepts

- **Probability Mass Function (PMF)**:
  - Discrete: P(X = x) = P(X takes on the value x)
  - Continuous: f(x) = probability density function (PDF)
- **Probability Density Function (PDF)**:
  - Continuous: f(x) ≥ 0 for all x in the domain
  - Integral of f(x) over the domain equals 1
- **Expected Value (E)**:
  - Discrete: E(X) = ∑xP(X = x)
  - Continuous: E(X) = ∫xf(x)dx
- **Variance (σ^2)**:
  - Discrete: σ^2 = E(X^2) - (E(X))^2
  - Continuous: σ^2 = E(X^2) - (E(X))^2

### Important Formulas and Theorems

- **Law of Large Numbers (LLN)**:
  - For a sequence of independent and identically distributed (i.i.d.) random variables, the sample average converges to the population mean with probability 1.
- **Central Limit Theorem (CLT)**:
  - For a sequence of i.i.d. random variables with finite mean and variance, the distribution of the sample mean converges to a normal distribution as the sample size increases.
- **Chebyshev's Inequality**:
  - For any random variable X with finite mean and variance, P(|X - E(X)| ≥ kσ) ≤ 1/k^2

### Key Theorems

- **Theorem of Total Probability**:
  - For any event A and any partition of the sample space into disjoint events B1, B2, ..., Bn, P(A) = ∑P(A ∩ Bi) where i = 1, 2, ..., n
- **De Morgan's Laws**:
  - For any events A and B, P(A ∪ B) = P(A) + P(B) - P(A ∩ B) and P(A ∩ B) = P(A)P(B)
