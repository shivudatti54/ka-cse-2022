# Continuous Random Variables

## Introduction

In the previous module, we explored discrete random variables that take on countable values. However, many real-world phenomena in computing and data science require modeling quantities that can take any value within an interval. For instance, the time a CPU processor takes to complete a task, the amount of memory consumed by an application, the response time of a web server, or the temperature of a data center—none of these can be adequately described by discrete values alone.

Continuous random variables are random variables that can assume any value within a continuum or interval, typically real numbers. Unlike discrete random variables where we assign probabilities to specific values, with continuous random variables we assign probabilities to intervals. This fundamental distinction leads to several important mathematical consequences: the probability of the variable taking any exact value is zero, and we describe the distribution through probability density functions (PDFs) rather than probability mass functions (PMFs).

Understanding continuous random variables is essential for modern computing professionals. Statistical analysis of continuous data, machine learning algorithms that work with real-valued features, performance modeling of computer systems, and data science applications all rely heavily on the theory of continuous distributions. This topic forms the backbone of probability-based computing and will be extensively used in subsequent courses on statistics, algorithms, and data science.

## Key Concepts

### 1. Definition of Continuous Random Variable

A random variable X is said to be continuous if there exists a non-negative function f(x), defined for all real numbers x, such that for any interval [a, b] (where a ≤ b), the probability that X lies in this interval is given by:

**P(a ≤ X ≤ b) = ∫[a to b] f(x) dx**

The function f(x) is called the **probability density function (PDF)** of the continuous random variable X. The PDF satisfies two fundamental properties:

1. **Non-negativity**: f(x) ≥ 0 for all x ∈ ℝ
2. **Normalization**: ∫[-∞ to ∞] f(x) dx = 1

It is crucial to understand that for a continuous random variable, P(X = c) = 0 for any specific value c. This is because:

P(X = c) = P(c ≤ X ≤ c) = ∫[c to c] f(x) dx = 0

This explains why we compute probabilities for intervals rather than exact values when dealing with continuous distributions.

### 2. Cumulative Distribution Function (CDF)

The cumulative distribution function F(x) of a continuous random variable X is defined as:

**F(x) = P(X ≤ x) = ∫[-∞ to x] f(t) dt**

The CDF has the following important properties:

- F(x) is non-decreasing: if x₁ < x₂, then F(x₁) ≤ F(x₂)
- lim(x→-∞) F(x) = 0
- lim(x→∞) F(x) = 1
- P(a < X ≤ b) = F(b) - F(a)
- The PDF is the derivative of the CDF: f(x) = d/dx F(x), where F is differentiable

The relationship between PDF and CDF is fundamental—understanding this connection allows us to move between the two representations of a continuous distribution seamlessly.

### 3. Expected Value and Variance

The **expected value** (or mean) of a continuous random variable X with PDF f(x) is:

**E[X] = ∫[-∞ to ∞] x · f(x) dx**

The **variance** of X measures the spread of the distribution:

**Var(X) = E[X²] - (E[X])² = ∫[-∞ to ∞] x² f(x) dx - μ²**

The **standard deviation** is the square root of variance: σ = √Var(X)

These moments have the same interpretation as in the discrete case but are computed using integration instead of summation.

### 4. Uniform Distribution

The **continuous uniform distribution** is the simplest continuous distribution. A random variable X follows a uniform distribution on the interval [a, b], denoted X ~ U(a, b), if its PDF is:

**f(x) = 1/(b-a) for a ≤ x ≤ b**
**f(x) = 0 otherwise**

The CDF of U(a, b) is:
- F(x) = 0 for x < a
- F(x) = (x-a)/(b-a) for a ≤ x ≤ b
- F(x) = 1 for x > b

Key properties:
- Mean: E[X] = (a + b)/2
- Variance: Var(X) = (b-a)²/12

In computing, uniform distributions are used in random number generation, simulation studies, and as the foundation for various sampling techniques.

### 5. Exponential Distribution

The **exponential distribution** is one of the most important continuous distributions in computing and operations research. It models the time between independent events occurring at a constant average rate. A random variable X follows an exponential distribution with parameter λ > 0, denoted X ~ Exp(λ), if its PDF is:

**f(x) = λe^(-λx) for x ≥ 0**
**f(x) = 0 for x < 0**

The CDF is:
- F(x) = 0 for x < 0
- F(x) = 1 - e^(-λx) for x ≥ 0

Key properties:
- Mean: E[X] = 1/λ
- Variance: Var(X) = 1/λ²
- Memoryless property: P(X > s + t | X > s) = P(X > t) for all s, t ≥ 0

The exponential distribution is extensively used to model:
- Time between incoming requests to a web server
- Time between CPU burst completions
- Time between packet arrivals in network communications
- Lifetime of certain electronic components

### 6. Normal Distribution

The **normal distribution** (also called Gaussian distribution) is the most important continuous distribution in probability theory and statistics. A random variable X follows a normal distribution with parameters μ and σ², denoted X ~ N(μ, σ²), if its PDF is:

**f(x) = (1/(σ√(2π))) · e^(-(x-μ)²/(2σ²)) for -∞ < x < ∞**

Key properties:
- Mean: E[X] = μ
- Variance: Var(X) = σ²
- Symmetric about μ
- Bell-shaped curve
- The empirical rule: Approximately 68% within μ±σ, 95% within μ±2σ, 99.7% within μ±3σ

The **standard normal distribution** is N(0, 1). Any normal random variable can be transformed to standard normal using the **z-score transformation**:

**Z = (X - μ)/σ ~ N(0, 1)**

This transformation is fundamental to statistical inference and is extensively used in data science, machine learning, and experimental analysis.

## Examples

### Example 1: CPU Processing Time Analysis

Suppose the time (in milliseconds) that a CPU takes to process a certain type of request follows an exponential distribution with mean 50 ms. Find:
(a) The probability that a request takes more than 100 ms
(b) The probability that a request takes between 30 ms and 70 ms
(c) The variance of processing time

**Solution:**

Given: Mean = 50 ms, so λ = 1/Mean = 1/50 = 0.02

(a) P(X > 100) = 1 - P(X ≤ 100) = 1 - F(100) = 1 - (1 - e^(-0.02×100)) = e^(-2) ≈ 0.1353

(b) P(30 < X < 70) = F(70) - F(30) = (1 - e^(-0.02×70)) - (1 - e^(-0.02×30))
= e^(-0.6) - e^(-1.4) ≈ 0.5488 - 0.2466 = 0.3022

(c) Variance = 1/λ² = 1/(0.02)² = 1/0.0004 = 2500 ms²

This type of analysis is crucial for system performance prediction and capacity planning in computing infrastructure.

### Example 2: Normal Distribution Application in Data Analysis

The memory usage (in GB) of a database server during peak hours follows a normal distribution with mean 8 GB and standard deviation 2 GB.

(a) What is the probability that memory usage exceeds 12 GB?
(b) Find the 95th percentile of memory usage.
(c) If the server has 15 GB capacity, what is the probability of exceeding capacity?

**Solution:**

Given: μ = 8, σ = 2, X ~ N(8, 4)

(a) P(X > 12) = P(Z > (12-8)/2) = P(Z > 2) = 1 - Φ(2) ≈ 1 - 0.9772 = 0.0228

(b) For 95th percentile, find z such that Φ(z) = 0.95. From z-table, z ≈ 1.645
Using X = μ + zσ = 8 + 1.645(2) = 11.29 GB

(c) P(X > 15) = P(Z > (15-8)/2) = P(Z > 3.5) ≈ 0.0002

This analysis helps in capacity planning and identifying when server upgrades might be necessary.

### Example 3: Uniform Distribution in Simulation

A scheduling algorithm generates random time slices for processes. Suppose the quantum time assigned to each process is uniformly distributed between 10 ms and 50 ms. A particular process requires at least 30 ms to complete its CPU burst. What is the probability that it gets enough time in a single quantum?

**Solution:**

Given: X ~ U(10, 50), a = 10, b = 50
We need P(X ≥ 30)

Since for continuous distributions P(X ≥ 30) = P(X > 30) = 1 - F(30)
F(30) = (30-10)/(50-10) = 20/40 = 0.5

P(X ≥ 30) = 1 - 0.5 = 0.5

Alternatively: P(X ≥ 30) = (50-30)/(50-10) = 20/40 = 0.5

This calculation is useful for analyzing scheduling algorithms and their fairness properties.

## Exam Tips

1. **Remember the fundamental difference**: For continuous random variables, P(X = c) = 0 always. This is a common trick in exam questions—students often incorrectly assign probabilities to single points.

2. **PDF vs PMF distinction**: The PDF f(x) does not give probability at a point; it must be integrated over an interval. Also note that f(x) can be greater than 1 (unlike PMF values), as long as the integral equals 1.

3. **CDF properties**: Always verify that your computed CDF satisfies 0 ≤ F(x) ≤ 1 and is non-decreasing. This is a good self-check for answers.

4. **Memoryless property of exponential**: Remember P(X > s + t | X > s) = P(X > t). This unique property is often tested and distinguishes exponential from other distributions.

5. **Normal distribution standardization**: Always convert to standard normal (z-score) before using z-tables. The formula Z = (X - μ)/σ must be applied correctly.

6. **Integration skills**: Many exam questions require computing probabilities by integrating PDFs or expected values by integrating x·f(x). Practice basic integration techniques.

7. **Relationship between PDF and CDF**: If you're given the CDF, differentiate to get the PDF. If you're given the PDF, integrate to get the CDF. Know both directions.

8. **Uniform distribution is uniform**: For U(a, b), the probability of any subinterval is proportional to its length—P(X ∈ [c, d]) = (d-c)/(b-a).