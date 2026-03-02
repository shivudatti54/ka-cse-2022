# Probability Mass Function (PMF), Probability Density Function (PDF), and Cumulative Distribution Function (CDF)

## Introduction

In the study of probability theory for computing, understanding how to characterize and analyze random variables is fundamental to fields like algorithm analysis, machine learning, and data science. When we work with random phenomena in computer science—whether analyzing the execution time of algorithms, modeling network traffic, or predicting user behavior—we need precise mathematical tools to describe the likelihood of different outcomes.

Three critical concepts form the backbone of probability distributions: the Probability Mass Function (PMF) for discrete random variables, the Probability Density Function (PDF) for continuous random variables, and the Cumulative Distribution Function (CDF) that unifies both. These functions allow us to quantify uncertainty and make predictions in computational contexts. For instance, when analyzing quicksort's average-case complexity, we use probability distributions to determine expected running time. In machine learning, understanding probability distributions is essential for maximum likelihood estimation and Bayesian inference.

This topic connects directly to practical computing applications: hash table collision analysis uses discrete distributions, modeling CPU service times employs continuous distributions, and queueing theory relies heavily on cumulative probabilities. Mastering these concepts will enable you to model real-world computing problems mathematically and make data-driven decisions.

## Key Concepts

### Random Variables

A random variable X is a function that maps outcomes of a random experiment to real numbers. We distinguish between two types:

- **Discrete Random Variables**: Take countable values (e.g., number of packet losses, number of comparisons in search algorithms)
- **Continuous Random Variables**: Take uncountable values within an interval (e.g., processing time, memory usage, network latency)

### Probability Mass Function (PMF)

For a discrete random variable X, the Probability Mass Function p_X(x) defines the probability that X equals a specific value:

p_X(x) = P(X = x)

**Properties of PMF:**
1. Non-negativity: p_X(x) ≥ 0 for all x
2. Summation to one: Σ p_X(x) = 1 (sum over all possible values)
3. The probability of any event A is P(X ∈ A) = Σ_{x∈A} p_X(x)

**Example PMFs:**
- Bernoulli distribution: p_X(1) = p, p_X(0) = 1-p
- Binomial distribution: p_X(k) = C(n,k) × p^k × (1-p)^(n-k)
- Poisson distribution: p_X(k) = (λ^k × e^(-λ)) / k!

### Probability Density Function (PDF)

For a continuous random variable X, the Probability Density Function f_X(x) describes the relative likelihood of the variable taking on a given value. Importantly, for continuous variables, P(X = x) = 0 for any specific x—we can only talk about probabilities over intervals.

**Properties of PDF:**
1. Non-negativity: f_X(x) ≥ 0 for all x
2. Integration to one: ∫ f_X(x) dx = 1 (integral over entire support)
3. Probability of interval: P(a ≤ X ≤ b) = ∫_a^b f_X(x) dx

**Common PDFs in Computing:**
- Uniform distribution: f(x) = 1/(b-a) for a ≤ x ≤ b
- Exponential distribution: f(x) = λe^(-λx) for x ≥ 0
- Normal distribution: f(x) = (1/σ√2π) × e^(-(x-μ)²/2σ²)

### Cumulative Distribution Function (CDF)

The CDF F_X(x) provides the probability that the random variable X takes a value less than or equal to x:

F_X(x) = P(X ≤ x)

**Properties of CDF:**
1. Non-decreasing: x₁ < x₂ implies F_X(x₁) ≤ F_X(x₂)
2. Right-continuous: F_X(x) = F_X(x⁺)
3. Limits: lim_{x→-∞} F_X(x) = 0, lim_{x→∞} F_X(x) = 1

**Relationship with PMF and PDF:**

For discrete X: F_X(x) = Σ_{t≤x} p_X(t)

For continuous X: F_X(x) = ∫_{-∞}^x f_X(t) dt

Conversely, we can recover the PMF/PDF from the CDF:
- PMF: p_X(x) = F_X(x) - F_X(x⁻) (jump at x)
- PDF: f_X(x) = d/dx F_X(x) (where differentiable)

## Examples

### Example 1: PMF for Binary Search Comparisons

In binary search, let X be the number of comparisons needed to find a target in a sorted array of size n. Suppose n = 8 (3 levels deep). The possible values are 1, 2, or 3.

**Solution:**
- P(X = 1) = 1/8 (target found at root)
- P(X = 2) = 2/8 = 1/4 (found at level 2)
- P(X = 3) = 5/8 (found at level 3 or not found)

PMF: p_X(1) = 0.125, p_X(2) = 0.25, p_X(3) = 0.625

Verification: 0.125 + 0.25 + 0.625 = 1 ✓

Expected comparisons: E[X] = 1(0.125) + 2(0.25) + 3(0.625) = 2.5

### Example 2: PDF for Processing Time

The CPU processing time X (in milliseconds) for a task follows an exponential distribution with rate λ = 2 per millisecond. Find P(0.5 ≤ X ≤ 1.5).

**Solution:**

Given f_X(x) = λe^(-λx) = 2e^(-2x) for x ≥ 0

P(0.5 ≤ X ≤ 1.5) = ∫_{0.5}^{1.5} 2e^(-2x) dx
= [-e^(-2x)]_{0.5}^{1.5}
= -e^(-3) + e^(-1)
= e^(-1) - e^(-3)
≈ 0.3679 - 0.0498
≈ 0.3181

Thus, there's approximately a 31.81% chance the processing time falls between 0.5ms and 1.5ms.

### Example 3: CDF from PDF

Given f_X(x) = 2x for 0 ≤ x ≤ 1 (uniform distribution over [0,1] with density doubled), find F_X(0.7).

**Solution:**

For 0 ≤ x ≤ 1: F_X(x) = ∫₀^x 2t dt = [t²]₀^x = x²

Therefore, F_X(0.7) = (0.7)² = 0.49

Interpretation: P(X ≤ 0.7) = 0.49, meaning there's a 49% probability the random variable is at most 0.7.

## Exam Tips

1. **Identify variable type first**: Always determine whether the random variable is discrete or continuous—this dictates whether you use PMF or PDF.

2. **PMF vs PDF key difference**: Remember that for continuous variables, P(X = a) = 0, but the PDF f(a) can be non-zero. Students often confuse these.

3. **CDF properties are frequently tested**: Know that CDF is always non-decreasing, ranges from 0 to 1, and is right-continuous.

4. **Integration vs Summation**: Use integrals for continuous PDFs and sums for discrete PMFs. Don't mix them up!

5. **Verification step**: Always check that your PMF sums to 1 or PDF integrates to 1—this is the most common error examiners check for.

6. **Relationship formulas**: The fundamental theorem: F'(x) = f(x) for continuous, and F(x) = Σ p(x) for discrete. Know both directions.

7. **Computing probabilities from CDF**: P(a < X ≤ b) = F(b) - F(a) works for both discrete and continuous cases—very useful in exam problems.

8. **Uniform distribution special case**: For continuous uniform on [a,b], PDF = 1/(b-a) and CDF = (x-a)/(b-a) for a ≤ x ≤ b—memorize this pattern.