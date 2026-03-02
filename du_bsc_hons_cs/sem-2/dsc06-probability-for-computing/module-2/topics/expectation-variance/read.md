# Expectation and Variance

## Introduction

Expectation and variance are fundamental concepts in probability theory that quantify the central tendency and spread of random variables respectively. In the context of computing, these concepts play a crucial role in algorithm analysis, machine learning, data science, and performance evaluation. When we analyze algorithms, we often deal with random inputs, and understanding the expected behavior helps us make informed design decisions.

The **expected value** (or mathematical expectation) of a random variable represents the long-run average value of repetitions of the experiment it represents. For instance, when analyzing the average-case complexity of a randomized algorithm, we compute the expected number of operations it will perform. The **variance** measures how far a set of numbers is spread out from their average value, giving us insight into the reliability or consistency of a random process. In machine learning, variance helps us understand model sensitivity to training data.

These concepts form the backbone of statistical analysis in computer science and are essential for any serious practitioner in the field. This module will provide you with rigorous mathematical foundations and practical computing applications that will serve you throughout your career.

## Key Concepts

### Expected Value of a Discrete Random Variable

For a discrete random variable X taking values x₁, x₂, x₃, ... with probability mass function P(X = xᵢ) = pᵢ, the **expected value** (also called the mean or expectation) is defined as:

**E[X] = Σᵢ xᵢ · pᵢ**

This summation converges absolutely if Σᵢ |xᵢ| · pᵢ < ∞.

For a continuous random variable X with probability density function f(x), the expected value is:

**E[X] = ∫(-∞ to ∞) x · f(x) dx**

The expected value possesses several important properties:

1. **Linearity of Expectation**: E[aX + bY] = aE[X] + bE[Y] for any constants a, b
2. **E[E[X]] = E[X]**: The expectation of an expectation is itself
3. **E[c] = c** for any constant c

### Variance and Standard Deviation

The **variance** of a random variable X measures the dispersion of X around its mean μ = E[X]. It is defined as:

**Var(X) = E[(X - μ)²] = E[X²] - (E[X])²**

The second formula, known as the "computational formula," is often easier to calculate:

**Var(X) = E[X²] - (E[X])²**

The **standard deviation** is the square root of the variance:

**σ(X) = √Var(X)**

The standard deviation is in the same units as the random variable itself, making it more interpretable in practical applications.

### Properties of Variance

1. **Var(c) = 0** for any constant c
2. **Var(aX + b) = a²Var(X)** for constants a, b
3. **Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)**
4. If X and Y are independent, then **Var(X + Y) = Var(X) + Var(Y)**

### Covariance

The **covariance** between two random variables X and Y is defined as:

**Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]**

Covariance indicates the direction of the linear relationship between two variables. A positive covariance suggests that both variables tend to move together, while negative covariance indicates an inverse relationship.

### Important Theorems

**Chebyshev's Inequality**: For any random variable X with mean μ and standard deviation σ, for any k > 0:

**P(|X - μ| ≥ kσ) ≤ 1/k²**

This inequality provides a bound on how far X can deviate from its mean and is fundamental in proving the Weak Law of Large Numbers.

**Law of Total Expectation**: For any partition of the sample space {Bᵢ}:

**E[X] = Σᵢ E[X | Bᵢ] · P(Bᵢ)**

This is particularly useful in solving complex probability problems by conditioning on simpler events.

## Examples

### Example 1: Expected Value of a Dice Roll

**Problem**: A fair six-sided die is rolled. Find the expected value of the outcome.

**Solution**:

The random variable X represents the outcome of the die roll. The sample space is S = {1, 2, 3, 4, 5, 6}, and each outcome has probability 1/6.

Using the formula E[X] = Σᵢ xᵢ · pᵢ:

E[X] = 1·(1/6) + 2·(1/6) + 3·(1/6) + 4·(1/6) + 5·(1/6) + 6·(1/6)
     = (1+2+3+4+5+6)/6
     = 21/6
     = 3.5

**Interpretation**: While we cannot roll a 3.5 on a single die, if we roll the die a large number of times, the average of all outcomes will approach 3.5. This is the fundamental interpretation of expected value.

### Example 2: Variance Calculation for a Biased Coin

**Problem**: A biased coin has P(Heads) = 0.7 and P(Tails) = 0.3. Let X be the random variable that takes value 1 for Heads and 0 for Tails. Find the variance of X.

**Solution**:

First, find E[X]:
E[X] = 1·(0.7) + 0·(0.3) = 0.7

Next, find E[X²]:
Since X takes only values 0 and 1, X² = X
Therefore, E[X²] = E[X] = 0.7

Now apply the computational formula:
Var(X) = E[X²] - (E[X])²
       = 0.7 - (0.7)²
       = 0.7 - 0.49
       = 0.21

**Verification using definition**:
Var(X) = E[(X - 0.7)²]
       = (1-0.7)²·0.7 + (0-0.7)²·0.3
       = 0.09·0.7 + 0.49·0.3
       = 0.063 + 0.147
       = 0.21 ✓

The standard deviation is √0.21 ≈ 0.458.

### Example 3: Average Case Analysis of Linear Search

**Problem**: In linear search on an array of n elements, assume the element being searched for is equally likely to be at any position (including being absent). What is the expected number of comparisons required?

**Solution**:

Let X be the number of comparisons. If the element is at position i (1 ≤ i ≤ n), we need i comparisons. If the element is not present, we need n comparisons.

Since the element is equally likely to be at any of the n+1 positions:
P(X = i) = 1/(n+1) for i = 1, 2, ..., n
P(X = n) = 1/(n+1) (for "not present" case)

Using the formula:
E[X] = Σᵢ=1ⁿ i·(1/(n+1)) + n·(1/(n+1))
     = (1/(n+1)) · [Σᵢ=1ⁿ i + n]
     = (1/(n+1)) · [n(n+1)/2 + n]
     = (1/(n+1)) · [n(n+1)/2 + 2n/2]
     = (1/(n+1)) · [n(n+1+2)/2]
     = (1/(n+1)) · [n(n+3)/2]
     = n(n+3)/(2(n+1))
     ≈ n/2 for large n

**Interpretation**: On average, linear search requires approximately n/2 comparisons, which is why we often consider this for average-case analysis in algorithm design.

## Exam Tips

1. **Memorize the formulas**: The formulas E[X] = Σx·P(X=x), Var(X) = E[X²] - (E[X])² are essential and frequently tested.

2. **Use the computational formula for variance**: It avoids computing (X - μ)² for each value, saving time and reducing calculation errors.

3. **Remember linearity of expectation**: E[aX + b] = aE[X] + b holds regardless of whether X and Y are independent—this is not true for variance.

4. **Always check if variables are independent** before applying Var(X + Y) = Var(X) + Var(Y).

5. **Understand units**: Standard deviation is in the same units as X; variance is in squared units—know when to use each.

6. **Apply the Law of Total Expectation**: When faced with complex problems, try conditioning on simpler events to break down the calculation.

7. **Practice with real computing examples**: Understand how expectation and variance apply to algorithm analysis, as DU exams frequently include such application-based questions.

8. **Know the range of variance**: Variance is always non-negative (Var(X) ≥ 0), and for a constant random variable, it equals zero.