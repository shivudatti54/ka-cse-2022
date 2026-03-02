# **Central Limit Theorem and Confidence Limits for Unknown Mean**

## **Introduction**

In statistics, the Central Limit Theorem (CLT) is a fundamental concept that describes the behavior of sample means. It states that, given certain conditions, the distribution of sample means will be approximately normally distributed, regardless of the underlying distribution of the population. This theorem has far-reaching implications for statistical inference, including confidence interval construction.

## **Definition of CLT**

- The Central Limit Theorem (CLT) states that, given a sample of size n from a population with mean μ and standard deviation σ, the distribution of the sample mean (x̄) will be approximately normally distributed, i.e., x̄ ~ N(μ, σ^2/n), as n → ∞.
- The CLT assumes that the sample is randomly selected from the population and that the population has a finite variance (σ^2).

## **Conditions for CLT**

- **Independence**: The observations in the sample must be independent of each other.
- **Idempotence**: The sample size must be sufficiently large (n → ∞).
- **Normality of population distribution**: Although the CLT can be applied to any distribution, it is most useful when the underlying population distribution is normal.

## **Characteristics of CLT**

- **Asymptotic normality**: The sample mean will be approximately normally distributed as the sample size increases.
- **Consistency**: The sample mean will converge to the population mean as the sample size increases.
- **Efficiency**: The sample mean is an unbiased estimator of the population mean.

## **Confidence Limits for Unknown Mean**

- **Definition**: A confidence interval provides a range of values within which the true population mean is likely to lie.
- **Construction**: A confidence interval for the mean (μ) is constructed using the sample mean (x̄) and the standard error of the mean (SE).
- **Formula**: Confidence interval = x̄ ± (Z \* SE), where Z is the Z-score corresponding to the desired confidence level.

### Explanation of Confidence Limits

- **Z-score**: The Z-score corresponds to the desired confidence level and is used to construct the confidence interval.
- **Standard error of the mean (SE)**: The SE is a measure of the variability of the sample mean and is calculated as SE = σ / √n.
- **Margin of error**: The margin of error is the difference between the upper and lower bounds of the confidence interval.

## **Example: Confidence Limits for Unknown Mean**

Suppose we want to construct a 95% confidence interval for the mean (μ) of a population with a known standard deviation (σ) of 10. We have a random sample of size n = 36 with a sample mean (x̄) of 25.

| Z-score | Confidence Interval |
| ------- | ------------------- |
| 1.96    | (23.4, 26.6)        |

In this example, the 95% confidence interval for the mean (μ) is (23.4, 26.6). This means that we are 95% confident that the true population mean lies within this interval.

## **Key Concepts**

- **Central Limit Theorem (CLT)**: states that the distribution of sample means will be approximately normally distributed, regardless of the underlying distribution of the population.
- **Confidence limits**: provide a range of values within which the true population mean is likely to lie.
- **Standard error of the mean (SE)**: a measure of the variability of the sample mean.
- **Z-score**: corresponds to the desired confidence level and is used to construct the confidence interval.

## **Practice Problems**

1.  A random sample of size n = 24 from a population with a known standard deviation (σ) of 8 has a sample mean (x̄) of 14. Construct a 90% confidence interval for the mean (μ) of the population.
2.  Suppose we want to construct a 99% confidence interval for the mean (μ) of a population with a known standard deviation (σ) of 12. We have a random sample of size n = 30 with a sample mean (x̄) of 18. Construct the confidence interval.

## **Conclusion**

In conclusion, the Central Limit Theorem (CLT) is a fundamental concept in statistics that describes the behavior of sample means. The CLT has far-reaching implications for statistical inference, including confidence interval construction. Understanding the CLT and confidence limits is essential for making informed decisions in a wide range of fields, including computer science, business, and medicine.
