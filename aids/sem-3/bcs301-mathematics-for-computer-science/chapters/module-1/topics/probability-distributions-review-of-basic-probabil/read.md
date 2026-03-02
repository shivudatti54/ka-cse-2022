# **Probability Distributions: Review of Basic Probability Theory**

## **Introduction**

Probability theory provides the foundation for probability distributions. In this study material, we will review the basic concepts of probability theory, including probability axioms, probability distributions, and their applications.

## **Probability Axioms**

The probability axioms are the fundamental principles of probability theory. They are:

- **Axiom 1: Probability is a number between 0 and 1**
  - P(X) ≥ 0 for all X
  - P(X) ≤ 1 for all X
- **Axiom 2: Probability is normalized**
  - P(X) = 1 for all X (the sample space)
- **Axiom 3: Countable additivity**
  - P(X ∪ Y) = P(X) + P(Y) - P(X ∩ Y) for all X and Y

## **Basic Probability Concepts**

### Expected Value

The expected value of a discrete random variable X is defined as:

E(X) = ∑xP(X=x)

where the sum is taken over all possible values of X.

### Variance

The variance of a discrete random variable X is defined as:

Var(X) = E(X^2) - [E(X)]^2

## **Common Probability Distributions**

### Uniform Distribution

A uniform distribution is a continuous probability distribution where every possible value has an equal probability.

- **Probability Density Function (PDF):**
  - f(x) = 1/(b-a) for a ≤ x ≤ b
  - f(x) = 0 otherwise

### Normal Distribution (Gaussian Distribution)

A normal distribution is a continuous probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean.

- **Probability Density Function (PDF):**
  - f(x) = (1/√(2πσ^2)) \* e^(-((x-μ)^2)/(2σ^2)) for -∞ < x < ∞
  - μ: mean
  - σ: standard deviation

### Binomial Distribution

A binomial distribution is a discrete probability distribution of the number of successes in a sequence of n independent experiments, each asking a yes–no question, and each with its own boolean-valued outcome: success (with probability p) or failure (with probability q = 1 − p).

- **Probability Mass Function (PMF):**
  - P(X = k) = (nCk) \* (p^k) \* (q^(n-k)) for k = 0 to n

### Poisson Distribution

A Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space if these events occur with a known average rate and independently of the time since the last event.

- **Probability Mass Function (PMF):**
  - P(X = k) = (e^(-λ) \* (λ^k)) / k! for k = 0 to ∞

### Key Concepts

---

- **Random Variable:** a variable whose possible values are determined by chance events
- **Random Sample:** a sample of data that is drawn randomly from a population
- **Probability Distribution:** a function that describes the probability of each possible value of a random variable

### Applications

---

- **Statistical Analysis:** probability distributions are used to analyze and understand data
- **Engineering:** probability distributions are used to design and optimize systems
- **Economics:** probability distributions are used to model and analyze economic systems

## **Conclusion**

In this study material, we reviewed the basic concepts of probability theory, including probability axioms, probability distributions, and their applications. We covered common probability distributions, including the uniform distribution, normal distribution, binomial distribution, and Poisson distribution. We also discussed key concepts, such as random variables, random samples, and probability distributions. Understanding probability theory is essential for working in fields such as computer science, engineering, and economics.
