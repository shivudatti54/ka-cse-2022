# **Joint Probability Distribution for Two Discrete Random Variables**

## **Introduction**

In probability theory, a joint probability distribution is a mathematical description of the probability of two or more discrete random variables taking on certain values. In this study material, we will focus on the joint probability distribution for two discrete random variables.

## **Definition**

The joint probability distribution of two discrete random variables X and Y is a function P(X, Y) that assigns a probability to each possible pair of values (x, y) of X and Y.

## **Mathematical Representation**

The joint probability distribution of X and Y can be represented as:

P(X = x, Y = y) = P(X = x) \* P(Y = y)

where P(X = x) and P(Y = y) are the marginal probability distributions of X and Y, respectively.

## **Key Concepts**

- **Joint Probability Mass Function (PMF)**: A function P(X, Y) that assigns a probability to each possible pair of values (x, y) of X and Y.
- **Marginal Probability Distribution**: The probability distribution of one of the random variables, obtained by summing over the other variable.
- **Conditional Probability**: The probability of one random variable given the value of the other random variable.

## **Example**

Suppose we have two discrete random variables X and Y, where X can take on values {1, 2, 3} and Y can take on values {A, B, C}. The joint probability distribution of X and Y can be represented as:

| X (X = 1) | X (X = 2) | X (X = 3) | | Y (Y = A) | Y (Y = B) | Y (Y = C) | |
|-----------|-----------|-----------| |-----------|-----------|-----------| |
| P(X = 1, Y = A) = 0.2 | P(X = 1, Y = B) = 0.1 | P(X = 1, Y = C) = 0.1 | | P(X = 2, Y = A) = 0.3 | P(X = 2, Y = B) = 0.2 | P(X = 2, Y = C) = 0.1 | |
| P(X = 2, Y = A) = 0.1 | P(X = 2, Y = B) = 0.2 | P(X = 2, Y = C) = 0.1 | | P(X = 3, Y = A) = 0.1 | P(X = 3, Y = B) = 0.2 | P(X = 3, Y = C) = 0.1 | |

In this example, the joint probability distribution of X and Y is represented by the table above.

## **Derivation of Marginal Probability Distributions**

The marginal probability distributions of X and Y can be obtained by summing over the other variable.

For example, the marginal probability distribution of X is obtained by summing over Y:

P(X = 1) = P(X = 1, Y = A) + P(X = 1, Y = B) + P(X = 1, Y = C) = 0.2 + 0.1 + 0.1 = 0.4

Similarly, the marginal probability distribution of Y is obtained by summing over X:

P(Y = A) = P(X = 1, Y = A) + P(X = 2, Y = A) + P(X = 3, Y = A) = 0.2 + 0.1 + 0.1 = 0.4

## **Conditional Probability**

The conditional probability of one random variable given the value of the other random variable can be calculated using the joint probability distribution.

For example, the conditional probability of X given Y = A is:

P(X = 1 | Y = A) = P(X = 1, Y = A) / P(Y = A) = 0.2 / 0.4 = 0.5

Similarly, the conditional probability of Y given X = 1 is:

P(Y = A | X = 1) = P(X = 1, Y = A) / P(X = 1) = 0.2 / 0.4 = 0.5

## **Conclusion**

In conclusion, the joint probability distribution of two discrete random variables is a powerful tool for analyzing and modeling complex probability problems. By understanding the joint probability distribution, we can derive marginal probability distributions and conditional probabilities, which are essential in many areas of computer science, including machine learning, data mining, and statistical inference.
