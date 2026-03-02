# **Central Limit Theorem and Confidence Limits for Unknown Mean**

## **Introduction**

The Central Limit Theorem (CLT) is a fundamental concept in statistics that describes the distribution of sample means. It states that the distribution of sample means will be approximately normal, regardless of the original distribution of the population. This theorem has numerous applications in statistical inference, including confidence intervals for the population mean.

## **What is the Central Limit Theorem?**

The CLT states that if we have a large sample of independent and identically distributed (i.i.d.) random variables, the distribution of the sample mean will be approximately normal, with a mean equal to the population mean and a variance equal to the population variance divided by the sample size.

## **Mathematical Definition**

Let X1, X2, ..., Xn be a random sample of size n from a population with mean μ and variance σ^2. The sample mean is defined as:

X̄ = (1/n) \* ∑Xi

The CLT states that:

n(X̄ - μ)^2 / σ^2 → χ^2(n) as n → ∞

where χ^2(n) is a chi-squared distribution with n degrees of freedom.

## **Properties of the Central Limit Theorem**

- **Asymptotic Normality**: The distribution of the sample mean will be approximately normal, regardless of the original distribution of the population.
- **Consistency**: The sample mean will converge to the population mean as the sample size increases.
- **Independence**: The sample mean is independent of the sample variance.

## **Confidence Limits for Unknown Mean**

A confidence interval for the population mean is a range of values within which the true population mean is likely to lie. The confidence interval is calculated using the sample mean and sample standard deviation.

## **Mathematical Definition**

Let X1, X2, ..., Xn be a random sample of size n from a population with mean μ and variance σ^2. The confidence interval for the population mean is defined as:

X̄ ± (Z \* (σ / √n))

where:

- X̄ is the sample mean
- Z is the Z-score corresponding to the desired confidence level
- σ is the sample standard deviation
- n is the sample size

## **Types of Confidence Intervals**

- **One-Sided Confidence Interval**: Used when the population mean is known to be positive or negative.
- **Two-Sided Confidence Interval**: Used when the population mean is unknown.

## **Example**

Suppose we want to estimate the population mean of the number of hours students spend studying per week. We take a random sample of 30 students and record the number of hours they spend studying per week. The sample mean is 4 hours, and the sample standard deviation is 1.5 hours.

Using a two-sided confidence interval with a confidence level of 95%, we can calculate the interval as follows:

X̄ ± (Z \* (σ / √n))
4 ± (1.96 \* (1.5 / √30))
4 ± (0.64)
(3.36, 4.64)

This interval suggests that the true population mean is likely to lie between 3.36 and 4.64 hours per week.

## **Key Concepts**

- **Sample mean**: The average value of a sample.
- **Sample standard deviation**: A measure of the spread or dispersion of a sample.
- **Confidence interval**: A range of values within which the true population mean is likely to lie.
- **Z-score**: A measure of how many standard deviations an element is from the mean.
- **Chi-squared distribution**: A probability distribution used to model the distribution of sample variances.

## **Conclusion**

The Central Limit Theorem is a fundamental concept in statistics that describes the distribution of sample means. It has numerous applications in statistical inference, including confidence intervals for the population mean. By understanding the CLT and confidence limits, you can make informed decisions about statistical analysis and inference.
