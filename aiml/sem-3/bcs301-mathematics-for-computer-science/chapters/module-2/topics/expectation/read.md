# Expectation (Mathematical Expectation)

## Introduction

Expectation, also known as expected value or mathematical expectation, is one of the most fundamental concepts in probability theory and statistics. It represents the long-run average value of a random variable when an experiment is repeated an infinite number of times. The concept of expectation bridges the gap between probability distributions and real-world applications, allowing us to quantify uncertain outcomes in fields such as finance, insurance, game theory, and statistical inference.

In the context of the DU Computer Science curriculum, understanding expectation is crucial because it forms the foundation for more advanced topics like variance, covariance, correlation, and moment-generating functions. Furthermore, expectation plays a vital role in Markov Chains, particularly in computing stationary distributions and expected return times. This topic connects directly with other concepts in Module 2, including joint probability distributions and stochastic processes, making it essential for both theoretical understanding and practical applications.

The study of expectation dates back to the 17th century when mathematicians like Pascal and Fermat were analyzing gambling problems. Today, it has evolved into a sophisticated mathematical tool used extensively in data science, machine learning, and algorithm analysis. For computer science students, expectation helps in analyzing randomized algorithms, computing average-case complexities, and understanding probabilistic data structures.

## Key Concepts

### Definition of Expected Value for Discrete Random Variables

For a discrete random variable X taking values x₁, x₂, x₃, ... with probability mass function P(X = xᵢ) = pᵢ, the expected value or mathematical expectation is defined as:

E[X] = Σᵢ xᵢ · pᵢ

The expectation exists (is finite) if Σᵢ |xᵢ| · pᵢ < ∞. This condition ensures that the sum converges absolutely, making the expectation well-defined regardless of the order of summation.

### Expected Value for Continuous Random Variables

For a continuous random variable X with probability density function f(x), the expected value is defined as:

E[X] = ∫₋∞^∞ x · f(x) dx

The integral must converge absolutely for the expectation to exist.

### Expectation of a Function of a Random Variable

If g(X) is a function of a random variable X, then:

For discrete case: E[g(X)] = Σᵢ g(xᵢ) · pᵢ

For continuous case: E[g(X)] = ∫ g(x) · f(x) dx

This property is crucial because it allows us to compute expectations of transformed random variables without finding their distribution first.

### Properties of Expectation

1. **Linearity of Expectation**: E[aX + bY] = aE[X] + bE[Y], where a and b are constants. This holds regardless of whether X and Y are independent or not.

2. **Expectation of a Constant**: E[c] = c for any constant c.

3. **Non-negativity**: If X ≥ 0, then E[X] ≥ 0.

4. **Expectation of Product (Independence)**: If X and Y are independent random variables, then E[XY] = E[X] · E[Y]. The converse is not necessarily true.

### Variance and Standard Deviation

Variance measures the spread of a random variable around its mean and is defined as:

Var(X) = E[(X - E[X])²] = E[X²] - (E[X])²

The standard deviation is the square root of variance: σ(X) = √Var(X)

### Covariance

Covariance measures the joint variability of two random variables:

Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]

If Cov(X, Y) = 0, the variables are uncorrelated (but not necessarily independent).

### Law of Total Expectation (Iterated Expectation)

For two random variables X and Y:
E[E[X|Y]] = E[X]

This is also known as the tower property and is extremely useful in conditional probability problems.

### Expected Value in Joint Distributions

For two discrete random variables X and Y with joint probability mass function p(x, y):

E[g(X, Y)] = Σₓ Σᵧ g(x, y) · p(x, y)

In particular:
E[X] = Σₓ Σᵧ x · p(x, y)
E[Y] = Σₓ Σᵧ y · p(x, y)

## Examples

### Example 1: Expected Value of a Die Roll

**Problem**: Find the expected value when rolling a fair six-sided die.

**Solution**:

The random variable X represents the outcome of the die roll. X can take values {1, 2, 3, 4, 5, 6}, each with probability 1/6.

E[X] = Σᵢ xᵢ · pᵢ = 1(1/6) + 2(1/6) + 3(1/6) + 4(1/6) + 5(1/6) + 6(1/6)
E[X] = (1+2+3+4+5+6)/6 = 21/6 = 3.5

**Interpretation**: While we can never roll exactly 3.5 on a single die, if we roll the die many times, the average outcome approaches 3.5.

### Example 2: Expectation of a Binomial Distribution

**Problem**: A biased coin has probability p = 0.6 of landing heads. If we toss the coin n = 5 times, find the expected number of heads.

**Solution**:

Let X ~ Binomial(n = 5, p = 0.6). The probability mass function is:
P(X = k) = C(5,k) · (0.6)^k · (0.4)^(5-k)

Using the linearity of expectation:
Each single toss can be modeled as a Bernoulli random variable Xᵢ where Xᵢ = 1 if heads, 0 if tails.
E[Xᵢ] = 1(p) + 0(1-p) = p = 0.6

X = X₁ + X₂ + X₃ + X₄ + X₅
E[X] = E[X₁] + E[X₂] + E[X₃] + E[X₄] + E[X₅] = 5 × 0.6 = 3

**Alternative verification**: Computing directly:
E[X] = Σₖ k · C(5,k) · (0.6)^k · (0.4)^(5-k) = 3

The expected number of heads is 3.

### Example 3: Expectation of a Function of Two Random Variables

**Problem**: Two random variables X and Y have the following joint probability distribution:

| X\Y | y=0 | y=1 |
|-----|-----|-----|
| x=0 | 0.1 | 0.2 |
| x=1 | 0.3 | 0.4 |

Find E[X + Y] and E[XY].

**Solution**:

First, verify this is a valid probability distribution:
0.1 + 0.2 + 0.3 + 0.4 = 1.0 ✓

**Computing E[X + Y]**:
E[X + Y] = Σₓ Σᵧ (x + y) · p(x,y)
= (0+0)(0.1) + (0+1)(0.2) + (1+0)(0.3) + (1+1)(0.4)
= 0 + 0.2 + 0.3 + 0.8 = 1.3

**Computing E[XY]**:
E[XY] = Σₓ Σᵧ (xy) · p(x,y)
= (0×0)(0.1) + (0×1)(0.2) + (1×0)(0.3) + (1×1)(0.4)
= 0 + 0 + 0 + 0.4 = 0.4

**Verification using marginal distributions**:
P(X=0) = 0.1 + 0.2 = 0.3
P(X=1) = 0.3 + 0.4 = 0.7
E[X] = 0(0.3) + 1(0.7) = 0.7

P(Y=0) = 0.1 + 0.3 = 0.4
P(Y=1) = 0.2 + 0.4 = 0.6
E[Y] = 0(0.4) + 1(0.6) = 0.6

E[X] + E[Y] = 0.7 + 0.6 = 1.3 ✓ (matches E[X + Y] by linearity)

## Exam Tips

1. **Remember the definition formula**: For discrete random variables, E[X] = Σ x·P(X=x). For continuous, E[X] = ∫ x·f(x)dx. Always identify the correct type of random variable first.

2. **Use linearity of expectation extensively**: E[aX + bY] = aE[X] + bE[Y] holds even when X and Y are dependent. This is the most powerful property and simplifies many calculations.

3. **Know the variance formula shortcut**: Var(X) = E[X²] - (E[X])². Computing E[X²] is often easier than computing E[(X-μ)²] directly.

4. **Distinguish between independence and uncorrelatedness**: If X and Y are independent, they are uncorrelated (Cov = 0), but the converse is not always true. This is a common exam question.

5. **Apply Law of Total Expectation**: E[E[X|Y]] = E[X] is extremely useful in problems involving conditional distributions, especially in two-stage random processes.

6. **For joint distributions, compute marginal expectations**: Find E[X] and E[Y] from joint distribution by summing appropriately: E[X] = Σₓ Σᵧ x·p(x,y).

7. **Check if expectation exists**: For infinite discrete or continuous distributions, the sum/integral must converge absolutely. If Σ|x|·p(x) diverges, the expectation does not exist.

8. **Link to Markov Chains**: In Markov Chains, expected time to reach a state and stationary distributions both rely on expectation concepts. Understand how to set up these calculations.