# Independent Random Variables

## Introduction

In probability theory and its applications to computing, understanding the concept of independent random variables is fundamental to modeling complex systems, analyzing algorithms, and making statistical inferences. Two random variables are said to be independent if the occurrence or value of one provides no information about the other. This seemingly simple concept has profound implications in computer science, particularly in areas such as cryptography, randomized algorithms, machine learning, and data analysis.

In this topic, we will explore the mathematical definition of independence, learn how to verify independence between random variables, examine important properties, and work through practical examples. Understanding independence is crucial for DU Computer Science students as it forms the backbone of many computational techniques, from Monte Carlo methods to statistical hypothesis testing. We will also explore how independence relates to other important concepts like covariance and correlation, which are essential for understanding dependencies in data.

## Key Concepts

### Definition of Independent Random Variables

Two discrete random variables X and Y are said to be independent if and only if their joint probability distribution equals the product of their marginal probability distributions. Mathematically, for all possible values x and y:

**P(X = x AND Y = y) = P(X = x) × P(Y = y)**

This can be compactly written as:
**P(X = x, Y = y) = P(X = x) · P(Y = y)**

For continuous random variables X and Y with joint density function f(x, y) and marginal densities f_X(x) and f_Y(y), independence means:

**f(x, y) = f_X(x) × f_Y(y)** for all x, y

Equivalently, the conditional distribution of Y given X = x is the same as the unconditional distribution of Y:
**P(Y ≤ y | X = x) = P(Y ≤ y)** for all x, y

This mathematical condition captures the intuitive idea that knowing the value of X tells us nothing about Y.

### Verifying Independence

To verify that two random variables are independent, we must check the condition for ALL possible pairs of values. This is a crucial point that students often miss—checking only a few values is insufficient. The steps to verify independence are:

1. Compute the marginal distributions P(X = x) for all x by summing over all y values
2. Compute the marginal distributions P(Y = y) for all y by summing over all x values
3. For each pair (x, y), verify that P(X = x, Y = y) = P(X = x) × P(Y = y)

If this equality holds for every pair, the variables are independent. If it fails for even one pair, they are dependent.

### Properties of Independent Random Variables

**Property 1: Expectation of Product**
If X and Y are independent random variables, then:
**E[XY] = E[X] × E[Y]**

This is one of the most useful properties of independence and is frequently used in computations.

**Property 2: Variance of Sum**
For independent random variables X and Y:
**Var(X + Y) = Var(X) + Var(Y)**

This additive property of variance holds only when X and Y are independent. If they are dependent, we must add the covariance term: Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X, Y).

**Property 3: Covariance**
If X and Y are independent, then **Cov(X, Y) = 0**. This is because:
Cov(X, Y) = E[XY] - E[X]E[Y] = E[X]E[Y] - E[X]E[Y] = 0

However, the converse is NOT true: zero covariance does NOT imply independence. Two random variables can have zero covariance but still be dependent (e.g., X and X² when X is symmetric around zero).

**Property 4: Sum of Independent Variables**
If X and Y are independent discrete random variables, the probability mass function of their sum Z = X + Y is given by the convolution:
**P(Z = z) = Σₓ P(X = x) × P(Y = z - x)**

For continuous independent variables, the convolution formula is:
**f_Z(z) = ∫ f_X(x) × f_Y(z - x) dx**

This property is fundamental in many applications, including the analysis of aggregate computational load.

### Independent Random Variables in Computing

In computer science, independent random variables appear in numerous contexts:

- **Hash Functions**: In hash table analysis, assuming hash values are independent helps in proving expected constant-time operations
- **Randomized Algorithms**: Many randomized algorithms rely on independence of random bits or random choices to analyze expected running time
- **Cryptography**: Independence of random seeds and keys is essential for security
- **Machine Learning**: Training data points are often assumed to be independent and identically distributed (i.i.d.)
- **Network Traffic**: Packet arrivals are often modeled as independent events

## Examples

### Example 1: Discrete Independent Random Variables

Consider two independent fair six-sided dice rolls. Let X be the outcome of die 1 and Y be the outcome of die 2. Both follow a uniform distribution over {1, 2, 3, 4, 5, 6} with P(X = x) = 1/6 and P(Y = y) = 1/6 for all x, y.

Since the dice are independent:
P(X = 3, Y = 5) = P(X = 3) × P(Y = 5) = (1/6) × (1/6) = 1/36

The joint distribution is uniform over all 36 outcomes.

Now let's compute E[XY]:
E[X] = E[Y] = (1+2+3+4+5+6)/6 = 3.5
By the product property: E[XY] = E[X] × E[Y] = 3.5 × 3.5 = 12.25

We can verify this directly:
E[XY] = Σₓ Σᵧ xy × P(X=x, Y=y) = (1/36) × Σₓ Σᵧ xy
= (1/36) × [36 terms ranging from 1×1 to 6×6]
= 12.25 ✓

### Example 2: Verifying Independence

Let the joint probability distribution of (X, Y) be given by:

| X\Y | y=0 | y=1 | P(X=x) |
|-----|-----|-----|--------|
| x=0 | 1/4 | 1/4 | 1/2 |
| x=1 | 1/4 | 1/4 | 1/2 |
| P(Y=y) | 1/2 | 1/2 | 1 |

Check: P(X=0, Y=0) = 1/4 = P(X=0) × P(Y=0) = (1/2) × (1/2) = 1/4 ✓
P(X=0, Y=1) = 1/4 = (1/2) × (1/2) = 1/4 ✓
P(X=1, Y=0) = 1/4 = (1/2) × (1/2) = 1/4 ✓
P(X=1, Y=1) = 1/4 = (1/2) × (1/2) = 1/4 ✓

All conditions satisfied! X and Y are independent.

### Example 3: Continuous Independent Random Variables

Let X and Y be independent continuous random variables, both uniformly distributed on [0, 1]. Their densities are f_X(x) = 1 for x ∈ [0,1], and similarly f_Y(y) = 1.

The joint density is f(x, y) = f_X(x) × f_Y(y) = 1 × 1 = 1 for (x, y) ∈ [0,1] × [0,1].

Find the probability that X + Y ≤ 1, i.e., P(X + Y ≤ 1):

This is the area of the triangle where x + y ≤ 1 within the unit square. The area is 1/2.

So P(X + Y ≤ 1) = 1/2.

Alternatively, using convolution, the PDF of Z = X + Y for z ∈ [0, 1] is:
f_Z(z) = ∫₀ᵗ 1 dx = z

For z ∈ [1, 2]: f_Z(z) = ∫₀¹ 1 dx = 2 - z

This gives the triangular distribution, and P(Z ≤ 1) = ∫₀¹ z dz = 1/2 ✓

### Example 4: Application in Algorithm Analysis

Consider a randomized quicksort algorithm. Let X_i be the indicator variable that the i-th smallest element is compared to the pivot. These indicator variables are not independent (knowing about one comparison gives information about others). However, for analyzing the expected number of comparisons, we can sometimes break complex dependencies by considering independent random variables representing "random choices" made by the algorithm.

Suppose we have n independent random variables, each representing a random choice that takes O(1) time. If we want to analyze the total running time T = X₁ + X₂ + ... + Xₙ, and these X_i are independent, we can use linearity of expectation: E[T] = Σ E[X_i]. This is fundamental to analyzing randomized algorithms in CS.

## Exam Tips

1. **Always check ALL pairs**: When verifying independence, you must check the condition for every possible pair of values, not just a few examples.

2. **Know the counterexamples**: Remember that zero covariance does NOT imply independence. Be prepared to give counterexamples like X and X² when X is symmetric.

3. **Property application**: The formula E[XY] = E[X]E[Y] holds ONLY for independent variables. This is a common trick in exam questions—make sure to verify independence before using this property.

4. **Variance addition**: Remember that Var(X + Y) = Var(X) + Var(Y) only when X and Y are independent. Always check for independence first.

5. **Convolution for sums**: For the sum of independent discrete variables, use the convolution formula. Draw a table if needed to avoid errors.

6. **Marginal from joint**: When given a joint distribution, always compute marginals first to check independence systematically.

7. **Practical computing examples**: In DU exams, expect questions relating independence to computing applications like hash functions or algorithm analysis.

8. **Conditional probability approach**: An alternative way to check independence is to verify P(Y = y | X = x) = P(Y = y) for all x, y.