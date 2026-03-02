# Mean and Variance

### Introduction

In probability theory, the mean and variance of a random variable are two fundamental concepts used to describe the distribution of a variable. The mean, also known as the expected value, represents the central tendency of the data, while the variance measures the spread or dispersion of the data.

### Mean

#### Definition

The mean of a random variable X is denoted by μ (mu) and is calculated as the sum of all possible values of X multiplied by their respective probabilities:

μ = E(X) = ∑xP(X=x)

where x represents the possible values of X, and P(X=x) represents the probability of each value.

#### Formula

The formula for calculating the mean is:

μ = (1/n) \* ∑xP(X=x)

where n is the number of possible values of X.

#### Example

Suppose we have a random variable X that can take on the values 1, 2, and 3 with probabilities 1/3, 1/3, and 1/3, respectively. The mean of X is:

μ = E(X) = (1/3) \* 1 + (1/3) \* 2 + (1/3) \* 3
= 1 + 2 + 3
= 6

#### Central Limit Theorem

The central limit theorem states that the distribution of the mean of a large sample of independent and identically distributed random variables will be approximately normal, regardless of the original distribution of the variables.

### Variance

#### Definition

The variance of a random variable X is denoted by σ^2 (sigma squared) and is calculated as the sum of the squared differences between each value of X and the mean, multiplied by their respective probabilities:

σ^2 = E((X-μ)^2) = ∑(x-μ)^2P(X=x)

#### Formula

The formula for calculating the variance is:

σ^2 = (1/n) \* ∑(x-μ)^2P(X=x)

where n is the number of possible values of X.

#### Example

Using the same example as before, the variance of X is:

σ^2 = E((X-μ)^2) = (1/3) \* (1-6)^2 + (1/3) \* (2-6)^2 + (1/3) \* (3-6)^2
= (1/3) \* 25 + (1/3) \* 16 + (1/3) \* 9
= 25/3 + 16/3 + 9/3
= 50/3

#### Properties

The variance of a random variable has the following properties:

- The variance of a constant is zero.
- The variance of a linear combination of independent random variables is the sum of their variances.
- The variance of the sum of independent random variables is the sum of their variances.

### Relation Between Mean and Variance

The variance is related to the mean by the following formula:

Var(X) = E(X^2) - μ^2

This formula shows that the variance is equal to the expected value of the square of the random variable minus the square of the mean.

### Conclusion

In conclusion, the mean and variance are two fundamental concepts in probability theory used to describe the distribution of a random variable. The mean represents the central tendency of the data, while the variance measures the spread or dispersion of the data. The relationship between the mean and variance is given by the formula Var(X) = E(X^2) - μ^2.
