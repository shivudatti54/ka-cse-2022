# Discrete Random Variables

## Introduction

Discrete Random Variables form the cornerstone of probability theory in computer science, with profound applications in algorithm analysis, machine learning, cryptography, and network communications. Unlike continuous variables that can take any value within an interval, discrete random variables assume only distinct, separate values—making them ideal for modeling countable phenomena such as the number of successful database queries, packet losses in a network, or defective items in a software release.

In the context of computing, understanding discrete random variables is essential for analyzing algorithmic complexity in randomized algorithms, modeling queueing systems in operating systems, and performing statistical inference in data science. The University of Delhi's Computer Science curriculum emphasizes this topic because it provides the mathematical foundation for more advanced subjects like Machine Learning, Artificial Intelligence, and Data Mining. This module will equip you with the tools to model uncertainty in computational processes and make data-driven decisions.

## Key Concepts

### Definition of Discrete Random Variable

A **discrete random variable** X is a function that maps outcomes of a random experiment to real numbers, where the set of possible values is either finite or countably infinite. Formally, X: Ω → ℝ where the image set {x : P(X = x) > 0} is either finite {x₁, x₂, ..., xₙ} or countably infinite {x₁, x₂, ...}.

**Key characteristic**: The values are separated by gaps—we cannot have values between two consecutive points.

### Probability Mass Function (PMF)

The **Probability Mass Function** (PMF) of a discrete random variable X is defined as pX(x) = P(X = x), specifying the probability that X takes a particular value. The PMF must satisfy two fundamental properties:

1. **Non-negativity**: pX(x) ≥ 0 for all x
2. **Normalization**: Σ pX(x) = 1, where the sum extends over all possible values of X

### Cumulative Distribution Function (CDF)

The **Cumulative Distribution Function** (CDF) of a discrete random variable X is defined as FX(x) = P(X ≤ x) = Σ pX(t) for all t ≤ x. For discrete variables, the CDF is a step function that jumps at each possible value of X, with the size of the jump equal to the probability mass at that point.

### Expected Value (Mean)

The **expected value** (or mathematical expectation, or mean) of a discrete random variable X is defined as:

E[X] = Σ x · pX(x)

The expected value represents the long-run average value of repetitions of the experiment. For a function g(X) of the random variable, E[g(X)] = Σ g(x) · pX(x).

**Properties of Expected Value**:
- E[aX + b] = aE[X] + b (linearity)
- E[X + Y] = E[X] + E[Y] (additivity)

### Variance and Standard Deviation

The **variance** of a discrete random variable X measures the spread of its distribution around the mean:

Var(X) = E[(X - μ)²] = E[X²] - (E[X])²

The **standard deviation** is σ = √Var(X), providing a measure of dispersion in the same units as the random variable itself.

**Properties of Variance**:
- Var(aX + b) = a² Var(X)
- Var(X) ≥ 0

### Common Discrete Distributions

#### 1. Bernoulli Distribution
A Bernoulli random variable models a single yes/no (success/failure) experiment with parameter p (probability of success).
- P(X = 1) = p, P(X = 0) = q = 1 - p
- E[X] = p
- Var(X) = p(1-p)

#### 2. Binomial Distribution
X ~ Bin(n, p) represents the number of successes in n independent Bernoulli trials.
- PMF: P(X = k) = C(n,k) · p^k · (1-p)^(n-k), for k = 0, 1, 2, ..., n
- E[X] = np
- Var(X) = np(1-p)

#### 3. Poisson Distribution
X ~ Poisson(λ) models the number of events occurring in a fixed interval of time/space when events occur with known constant mean rate λ.
- PMF: P(X = k) = (e^(-λ) · λ^k) / k!, for k = 0, 1, 2, ...
- E[X] = λ
- Var(X) = λ

#### 4. Geometric Distribution
X ~ Geom(p) represents the number of trials until the first success in independent Bernoulli trials.
- PMF: P(X = k) = (1-p)^(k-1) · p, for k = 1, 2, 3, ...
- E[X] = 1/p
- Var(X) = (1-p)/p²

## Examples

### Example 1: Analyzing Software Bug Detection

A software testing team estimates that each module has a 15% chance of containing a critical bug. For a project with 8 independent modules, let X represent the number of modules with critical bugs.

**Solution**:
Here X follows a Binomial distribution with n = 8, p = 0.15

(a) Probability that exactly 2 modules have bugs:
P(X = 2) = C(8,2) · (0.15)² · (0.85)⁶
= 28 · 0.0225 · 0.3771496637
≈ 0.2376

(b) Expected number of buggy modules:
E[X] = np = 8 × 0.15 = 1.2 modules

(c) Variance:
Var(X) = np(1-p) = 8 × 0.15 × 0.85 = 1.02

### Example 2: Network Server Requests

A web server receives on average 5 requests per minute. Using Poisson distribution with λ = 5:

**Solution**:

(a) Probability of exactly 3 requests in a minute:
P(X = 3) = (e^(-5) × 5³) / 3!
= (0.0067379 × 125) / 6
≈ 0.1404

(b) Probability of at least 2 requests:
P(X ≥ 2) = 1 - P(X ≤ 1)
= 1 - [P(0) + P(1)]
= 1 - [e^(-5) + 5·e^(-5)]
= 1 - e^(-5)(1 + 5)
= 1 - 0.0067379 × 6
≈ 0.9596

### Example 3: Expected Value and Variance Calculation

A discrete random variable X has the following PMF:
x: 0, 1, 2, 3
P(X=x): 0.1, 0.3, 0.4, 0.2

**Solution**:

First, verify normalization: 0.1 + 0.3 + 0.4 + 0.2 = 1.0 ✓

Expected value:
E[X] = Σ x·p(x) = 0(0.1) + 1(0.3) + 2(0.4) + 3(0.2)
= 0 + 0.3 + 0.8 + 0.6 = 1.7

E[X²] = Σ x²·p(x) = 0²(0.1) + 1²(0.3) + 2²(0.4) + 3²(0.2)
= 0 + 0.3 + 1.6 + 1.8 = 3.7

Variance:
Var(X) = E[X²] - (E[X])² = 3.7 - (1.7)² = 3.7 - 2.89 = 0.81

Standard Deviation: σ = √0.81 = 0.9

## Exam Tips

1. **Always verify PMF normalization**: Before solving any problem, confirm that Σ p(x) = 1. This catches calculation errors early.

2. **Identify the distribution first**: Recognize whether the problem follows Bernoulli, Binomial, Poisson, or Geometric patterns—this determines your entire approach.

3. **Use linearity of expectation**: For complex problems, break down X = X₁ + X₂ + ... + Xₙ where each Xᵢ is simpler, then use E[X] = Σ E[Xᵢ].

4. **Memorize mean and variance formulas**: For all four standard distributions (Bernoulli, Binomial, Poisson, Geometric), the expected value and variance are frequently tested.

5. **CDF calculation technique**: For P(a < X ≤ b), remember it's FX(b) - FX(a), not FX(b) - FX(a-1) for discrete variables.

6. **Poisson as Binomial limit**: When n is large and p is small with np = λ (constant), Binomial(n,p) ≈ Poisson(λ). This is useful for approximation problems.

7. **Variance shortcut**: Calculate E[X²] first, then compute variance using Var(X) = E[X²] - (E[X])²—this is often faster than computing (X - μ)² for each value.

8. **Units matter**: Standard deviation is in the same units as the random variable; variance is in squared units. Don't mix them up in interpretation.