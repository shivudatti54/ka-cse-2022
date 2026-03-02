# EXPECTATION

## Introduction

Expectation, also known as expected value or mathematical expectation, is one of the most fundamental concepts in probability theory and statistics. It serves as the central measure of a random variable, providing a single number that summarizes the long-run average outcome of a random phenomenon. In the context of the University of Delhi's Computer Science curriculum, understanding expectation is crucial because it forms the backbone of many advanced topics including statistical inference, machine learning algorithms, data analysis, and stochastic processes such as Markov Chains.

The concept of expectation originated from gambling problems in the 17th century, where mathematicians like Pascal and Fermat sought to analyze games of chance. Today, expectation finds applications in diverse fields such as finance (portfolio analysis), insurance (risk assessment), computer science (algorithm analysis), and physics (statistical mechanics). For Computer Science students at DU, particularly those preparing for careers in data science, artificial intelligence, or quantitative finance, a thorough understanding of expectation is absolutely essential.

This chapter explores the mathematical definition of expectation for both discrete and continuous random variables, examines its properties including the crucial linearity property, discusses expectation of functions of random variables, and introduces related concepts like variance, moments, and conditional expectation. These concepts will be particularly useful when studying joint probability distributions and later when analyzing Markov Chains in this module.

## Key Concepts

### Definition of Expected Value

The expected value of a discrete random variable X, denoted as E(X) or μ, is defined as the weighted average of all possible values that X can take, where the weights are the respective probabilities. Mathematically, for a discrete random variable X with possible values x₁, x₂, x₃, ... and probability mass function P(X = xᵢ) = pᵢ, the expected value is:

E(X) = Σᵢ xᵢ · pᵢ

This summation is taken over all possible values that the random variable can assume. The expected value exists (is finite) if the sum Σᵢ |xᵢ| · pᵢ converges.

For a continuous random variable X with probability density function f(x), the expected value is defined as:

E(X) = ∫₋∞^∞ x · f(x) dx

This integral must converge absolutely, meaning ∫₋∞^∞ |x| · f(x) dx < ∞, for the expectation to exist.

### Expectation of a Constant

If X is a constant random variable that always takes the value c (i.e., P(X = c) = 1), then:

E(c) = c

This is intuitive since if a quantity is always equal to c, its average value must be c.

### Linearity of Expectation

One of the most important and powerful properties of expectation is its linearity. For any random variables X and Y (not necessarily independent) and any constants a and b:

E(aX + bY) = aE(X) + bE(E) + bE(Y)

This property holds regardless of whether X and Y are independent. Additionally, for any constant c:

E(X + c) = E(X) + c

The linearity property makes expectation computationally very convenient and is extensively used in statistical inference and probability theory.

### Expectation of Functions of Random Variables

If we have a random variable X and we want to find the expected value of some function g(X), we do not need to find the distribution of g(X) first. We can compute it directly using:

For discrete X: E[g(X)] = Σᵢ g(xᵢ) · P(X = xᵢ)

For continuous X: E[g(X)] = ∫₋∞^∞ g(x) · f(x) dx

This is known as the "law of the unconscious statistician" (LOTUS).

### Variance and Standard Deviation

While expectation provides information about the central tendency of a distribution, it tells us nothing about the spread or dispersion of values. The variance of a random variable X, denoted as Var(X) or σ², measures this dispersion and is defined as:

Var(X) = E[(X - E(X))²] = E(X²) - [E(X)]²

The second formula is often computationally easier and is derived from expanding the square. The standard deviation, σ, is the square root of the variance and is in the same units as X.

Important properties of variance include:

- Var(aX + b) = a² Var(X) where a and b are constants
- Var(X) ≥ 0 always
- Var(X) = 0 if and only if X is a constant (almost surely)

### Moments

Moments are expectations of powers of the random variable. The nth moment of X is E(Xⁿ). The first moment is simply the mean E(X). The second central moment is the variance. Moments provide a complete description of a probability distribution in many cases (through the moment-generating function).

The nth central moment is E[(X - E(X))ⁿ], which measures the shape of the distribution around its mean.

### Covariance and Correlation

When dealing with two random variables X and Y, we need to measure their joint behavior. The covariance between X and Y is defined as:

Cov(X, Y) = E[(X - E(X))(Y - E(Y))] = E(XY) - E(X)E(Y)

Covariance indicates the direction of the linear relationship between two variables. A positive covariance suggests that both variables tend to be above or below their means together, while negative covariance indicates an inverse relationship.

The correlation coefficient ρ(X, Y) normalizes the covariance to a dimensionless quantity between -1 and 1:

ρ(X, Y) = Cov(X, Y) / [√Var(X) · √Var(Y)]

Correlation measures the strength and direction of the linear relationship between variables.

### Conditional Expectation

Conditional expectation is the expected value of a random variable given information about another variable. For discrete random variables:

E(X|Y = y) = Σᵢ xᵢ · P(X = xᵢ | Y = y)

The law of total expectation (or law of iterated expectations) states:

E[E(X|Y)] = E(X)

This is a fundamental result that states the unconditional expectation can be obtained by first taking the expectation conditional on another variable and then taking the expectation of that result.

## Examples

### Example 1: Expected Value of a Die Roll

Consider the experiment of rolling a fair six-sided die. Let X be the outcome of the roll. The probability distribution is P(X = i) = 1/6 for i = 1, 2, 3, 4, 5, 6.

Solution:
E(X) = Σᵢ₌₁⁶ i · (1/6)
E(X) = (1 + 2 + 3 + 4 + 5 + 6) / 6
E(X) = 21 / 6
E(X) = 3.5

This result shows that while we can never roll a 3.5 on a single die, the long-run average of many rolls approaches 3.5. This is the fundamental interpretation of expected value.

### Example 2: Expectation of a Function

Let X be a discrete random variable with the following probability distribution:

P(X = -2) = 0.2, P(X = 0) = 0.5, P(X = 3) = 0.3

Find E(X²) and E(3X + 1).

Solution:
Using the law of the unconscious statistician:

E(X²) = Σ g(xᵢ) · P(X = xᵢ)
E(X²) = (-2)² · 0.2 + (0)² · 0.5 + (3)² · 0.3
E(X²) = 4 · 0.2 + 0 · 0.5 + 9 · 0.3
E(X²) = 0.8 + 0 + 2.7
E(X²) = 3.5

For E(3X + 1):
E(3X + 1) = 3E(X) + 1 (by linearity)
First find E(X):
E(X) = (-2) · 0.2 + 0 · 0.5 + 3 · 0.3
E(X) = -0.4 + 0 + 0.9 = 0.5
Therefore, E(3X + 1) = 3(0.5) + 1 = 1.5 + 1 = 2.5

We can verify directly:
E(3X + 1) = (3(-2) + 1) · 0.2 + (3(0) + 1) · 0.5 + (3(3) + 1) · 0.3
E(3X + 1) = (-6 + 1) · 0.2 + 1 · 0.5 + (9 + 1) · 0.3
E(3X + 1) = (-5) · 0.2 + 0.5 + 10 · 0.3
E(3X + 1) = -1 + 0.5 + 3 = 2.5 ✓

### Example 3: Variance Calculation

Using the same random variable from Example 2, calculate Var(X).

Solution:
We already have E(X) = 0.5 and E(X²) = 3.5

Using the formula: Var(X) = E(X²) - [E(X)]²
Var(X) = 3.5 - (0.5)²
Var(X) = 3.5 - 0.25
Var(X) = 3.25

The standard deviation is √3.25 ≈ 1.803

Alternatively, we can compute variance directly:
Var(X) = E[(X - E(X))²]
= Σ (xᵢ - 0.5)² · P(X = xᵢ)
= (-2 - 0.5)² · 0.2 + (0 - 0.5)² · 0.5 + (3 - 0.5)² · 0.3
= (-2.5)² · 0.2 + (-0.5)² · 0.5 + (2.5)² · 0.3
= 6.25 · 0.2 + 0.25 · 0.5 + 6.25 · 0.3
= 1.25 + 0.125 + 1.875
= 3.25 ✓

### Example 4: Application in Decision Making

A software company is deciding whether to launch a new product. If launched, there are three possible market responses: "High" with profit ₹500,000 (probability 0.3), "Medium" with profit ₹200,000 (probability 0.5), and "Low" with profit -₹100,000 (probability 0.2). If not launched, the profit is ₹0. Should the company launch the product based on expected value?

Solution:
Let X be the profit if the product is launched.
E(X) = 500,000 × 0.3 + 200,000 × 0.5 + (-100,000) × 0.2
E(X) = 150,000 + 100,000 - 20,000
E(X) = ₹230,000

Since E(X) > ₹0 (the expected profit from not launching), the company SHOULD launch the product based on the expected value criterion.

This example demonstrates how expectation is used in business decision-making under uncertainty. However, note that real-world decisions might also consider risk tolerance—some decision-makers might prefer the guaranteed ₹0 over the risky expected gain of ₹230,000.

## Exam Tips

1. UNDERSTAND THE DEFINITION: Know how to compute expectation for both discrete and continuous random variables. The exam frequently asks for direct computation of E(X) from a given probability distribution.

2. REMEMBER LINEARITY: The property E(aX + bY) = aE(X) + bE(Y) is incredibly useful and works even when X and Y are dependent. USE THIS PROPERTY to simplify complex calculations.

3. KNOW LOTUS: The Law of the Unconscious Statistician allows you to find E[g(X)] without finding the distribution of g(X). Remember: for discrete: Σ g(xᵢ)pᵢ, for continuous: ∫ g(x)f(x)dx.

4. VARIANCE SHORTCUT: Use Var(X) = E(X²) - [E(X)]² to compute variance more efficiently rather than computing E[(X - μ)²].

5. COVARIANCE VS CORRELATION: Remember that covariance is not normalized and depends on the units of X and Y, while correlation is dimensionless and always lies between -1 and 1.

6. LAW OF TOTAL EXPECTATION: E[E(X|Y)] = E(X) is a crucial result. Understand its interpretation—it essentially says you can compute unconditional expectation by first conditioning on another variable.

7. INTERPRETATION: When answering conceptual questions, explain that expected value represents the long-run average if an experiment is repeated infinitely many times.

8. CHECK CONVERGENCE: For continuous distributions, ensure you mention that the expectation exists only when the integral converges absolutely.

9. COVARIANCE PROPERTIES: Remember Cov(X, X) = Var(X) and Cov(X, Y) = 0 if X and Y are independent.

10. PRACTICE PREVIOUS YEARS: DU exams often include questions on finding E(X), Var(X), and computing covariance for given joint distributions—practice these thoroughly.