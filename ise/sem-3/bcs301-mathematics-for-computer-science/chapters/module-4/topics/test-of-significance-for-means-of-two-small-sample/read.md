# Test of Significance for Means of Two Small Samples

## **Introduction**

In this topic, we will learn about the test of significance for means of two small samples. This test is used to determine if there is a significant difference between the means of two independent samples. The test is commonly used in computer science to evaluate the effectiveness of different algorithms or to compare the performance of different systems.

## **Mathematical Definition**

The test of significance for means of two small samples is based on the concept of hypothesis testing. The null hypothesis is that there is no significant difference between the means of the two samples, while the alternative hypothesis is that there is a significant difference.

## **Null and Alternative Hypotheses**

- **Null Hypothesis (H0):** μ1 = μ2 (The means of the two samples are equal)
- **Alternative Hypothesis (H1):** μ1 ≠ μ2 (The means of the two samples are not equal)

## **Test Statistic**

The test statistic is calculated as:

t = (x̄1 - x̄2) / sqrt((s1^2/n1) + (s2^2/n2))

where:

- x̄1 and x̄2 are the sample means
- s1^2 and s2^2 are the sample variances
- n1 and n2 are the sample sizes

## **Critical Region**

The critical region is the region of the test statistic where the null hypothesis is rejected. The critical region is typically located in the tails of the distribution, far away from the mean.

## **Level of Significance**

The level of significance is the probability of rejecting the null hypothesis when it is true. The level of significance is typically set to 0.05.

## **Types of Errors**

- **Type I Error:** Rejecting the null hypothesis when it is true (α)
- **Type II Error:** Failing to reject the null hypothesis when it is false (β)

## **Examples**

### Example 1:

Suppose we want to compare the average salary of two different groups of software engineers. Group 1 has a sample size of 10 and a sample mean of $80,000. Group 2 has a sample size of 12 and a sample mean of $90,000. We want to determine if there is a significant difference between the two means.

- **Null Hypothesis:** μ1 = μ2 (The means of the two groups are equal)
- **Alternative Hypothesis:** μ1 ≠ μ2 (The means of the two groups are not equal)

Using the formula above, we calculate the test statistic:

t = (80,000 - 90,000) / sqrt((10^2/10) + (12^2/12)) = -10 / sqrt(10 + 12) = -10 / sqrt(22) = -1.41

The critical region is typically located in the tails of the t-distribution, far away from the mean. Let's assume the level of significance is 0.05. The critical value for a two-tailed test is approximately ±2.086.

Since our test statistic (-1.41) is not in the critical region, we fail to reject the null hypothesis. There is no significant difference between the means of the two groups.

### Example 2:

Suppose we want to compare the average response time of two different algorithms. Algorithm 1 has a sample size of 20 and a sample mean of 10 seconds. Algorithm 2 has a sample size of 25 and a sample mean of 8 seconds. We want to determine if there is a significant difference between the two means.

- **Null Hypothesis:** μ1 = μ2 (The means of the two algorithms are equal)
- **Alternative Hypothesis:** μ1 ≠ μ2 (The means of the two algorithms are not equal)

Using the formula above, we calculate the test statistic:

t = (10 - 8) / sqrt((20^2/20) + (25^2/25)) = 2 / sqrt(20 + 25) = 2 / sqrt(45) = 0.67

Since our test statistic (0.67) is not in the critical region, we fail to reject the null hypothesis. There is no significant difference between the means of the two algorithms.

## **Conclusion**

In conclusion, the test of significance for means of two small samples is a statistical test used to determine if there is a significant difference between the means of two independent samples. The test is based on the concept of hypothesis testing and involves calculating a test statistic and comparing it to a critical value. The test can be used in a variety of fields, including computer science, to evaluate the effectiveness of different algorithms or to compare the performance of different systems.
