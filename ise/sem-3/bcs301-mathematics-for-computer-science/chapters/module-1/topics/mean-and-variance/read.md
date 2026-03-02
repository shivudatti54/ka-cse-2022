# **Mean and Variance**

## **Introduction**

In probability theory, the mean and variance are two fundamental concepts used to describe the distribution of a random variable. The mean represents the average value of the random variable, while the variance measures the spread or dispersion of the values from the mean.

## **Mean**

### Definition

The mean, also known as the expected value, is a measure of the central tendency of a random variable. It is calculated by summing up all the possible values of the variable and dividing by the number of possible values.

### Formula

E(X) = ∑xP(x)

where E(X) is the mean, x is the possible value of the variable, and P(x) is the probability of the variable taking the value x.

### Example

Suppose we roll a fair six-sided die. The possible values of the random variable X are 1, 2, 3, 4, 5, and 6, with equal probabilities of 1/6.

To calculate the mean:

E(X) = (1 × 1/6) + (2 × 1/6) + (3 × 1/6) + (4 × 1/6) + (5 × 1/6) + (6 × 1/6)
= 21/6
= 3.5

The mean of the random variable X is 3.5.

### Properties

- The mean is a linear function of the random variable, meaning that if X is a random variable, then aX + b is also a random variable, and E(aX + b) = aE(X) + b.
- The mean is a measure of central tendency, but it is not a measure of spread.

## **Variance**

### Definition

The variance is a measure of the spread or dispersion of a random variable. It is calculated by finding the average of the squared differences between each possible value of the variable and the mean.

### Formula

σ^2 = ∑(x - E(X))^2P(x)

where σ^2 is the variance, x is the possible value of the variable, E(X) is the mean, and P(x) is the probability of the variable taking the value x.

### Example

Using the same example as before, we can calculate the variance:

σ^2 = (1 - 3.5)^2(1/6) + (2 - 3.5)^2(1/6) + (3 - 3.5)^2(1/6) + (4 - 3.5)^2(1/6) + (5 - 3.5)^2(1/6) + (6 - 3.5)^2(1/6)
= 2.0833

The variance of the random variable X is approximately 2.0833.

### Properties

- The variance is a measure of spread, but it is not a measure of skewness.
- The variance is a positive quantity, meaning that the spread of the random variable is always non-negative.
- The variance is a measure of the "fitness" or "robustness" of a random variable, in the sense that a higher variance indicates a greater spread and therefore a greater uncertainty.

## **Relationship Between Mean and Variance**

The mean and variance are related by the following formula:

Var(X) = E(X^2) - E(X)^2

This formula shows that the variance is equal to the expected value of the square of the variable minus the square of the mean.

## **Key Concepts**

- Mean: a measure of central tendency, calculated as the average value of a random variable.
- Variance: a measure of spread or dispersion, calculated as the average of the squared differences between each possible value of the variable and the mean.
- Linearity: the mean is a linear function of the random variable.
- Properties of mean:
  - The mean is a linear function of the random variable.
  - The mean is a measure of central tendency, but not a measure of spread.
- Properties of variance:
  - The variance is a measure of spread, but not a measure of skewness.
  - The variance is a positive quantity.
  - The variance is a measure of the "fitness" or "robustness" of a random variable.
