# **Probability Distributions: Review of Basic Probability Theory**

### Definitions and Notations

- **Random Variable (RV):** A function that assigns a numerical value to each outcome of a random experiment.
- **Probability Distribution (PDF):** A function that describes the probability of each outcome of a random experiment.
- **Probability Mass Function (PMF):** A function that describes the probability of each outcome of a discrete random experiment.
- **Probability Density Function (PDF):** A function that describes the probability of each outcome of a continuous random experiment.

### Probability Rules

- **Complementary Rule:** P(A) = 1 - P(A')
- **Additive Rule:** P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- **Multiplicative Rule:** P(A ∩ B) = P(A) × P(B)

### Basic Probability Theorems

- **Axioms of Probability:**
  - Probability is a non-negative real number.
  - Probability is zero for impossible events.
  - Probability is one for certain events.
- **Countable Additivity:** If A and B are mutually exclusive, then P(A ∪ B) = P(A) + P(B)
- **Probability of the Union of Two Events:** P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

### Important Formulas

- **Probability of an Event:** P(A) = ∫f(x) dx (for continuous RVs)
- **Probability of a Discrete Event:** P(X = k) = P(k) (for discrete RVs)
- **Expectation (Mean):** μ = E(X) = ∑xP(x) (for discrete RVs)
- **Variance:** σ^2 = E(X^2) - μ^2 (for discrete RVs)

### Other Key Points

- **Uniform Distribution:** PDF = 1 / b - a, for a ∈ (a, b)
- **Normal Distribution:** PDF = (1 / √(2πσ^2)) × e^(-x^2 / 2σ^2), for x ∈ (-∞, ∞)
- **Binomial Distribution:** PMF = n! / (k!(n-k)!) × p^k \* (1-p)^(n-k), for x ∈ {0, 1, ..., n}
